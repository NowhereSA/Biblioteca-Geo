from fastapi import HTTPException, FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
#from bson import ObjectId
import database as db
import models as md
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def main(request: Request, skip=0, limit=10):
    books = []
    for book in db.collection.find().skip(skip).limit(limit):
        books.append({
            "id": str(book["id"]),
            "titulo": str(book["titulo"]), 
            "autor": str(book["autor"]),
            "genero": str(book["genero"]),
            "status": str(book["status"]),
            "descricao": str(book["descricao"])
        })
    context = {"request": request, "books": books}
    return md.templates.TemplateResponse("livros.html", context)


@app.get("/books", response_class=HTMLResponse)
async def show_book(request: Request, skip= 0, limit = 10):
    #books = list(collection.find({}, {"_id": 0})) # Id zero é para excluir todos ids (filtro) , {"_id": 0}
    books = []
    for book in db.collection.find().skip(skip).limit(limit):
        books.append({
            "id": int(book["id"]),
            "titulo": str(book["titulo"]), 
            "autor": str(book["autor"]),
            "genero": str(book["genero"]),
            "status": str(book["status"]),
            "descricao": str(book["descricao"])
        })
    return md.templates.TemplateResponse("main.html", {"request": request, "books": books})

@app.post("/books")
async def add_book(data: md.Annotated[md.Biblioteca, Form()]):
#async def add_book(data: md.Biblioteca):
    data_dict = data.model_dump(by_alias=True)
    result = db.collection.find_one({"titulo": data_dict["titulo"]})

    if result:
        if data_dict["titulo"] == result["titulo"]:
            raise HTTPException(status_code=400, detail="Já contém um livro igual.")
        
    else: 
        db.collection.create_index([("id", 1)], unique=True)
        data_dict["id"] = db.collection.count_documents({}) + 1

    db.collection.insert_one(data_dict)

    return RedirectResponse(
        url="/books",
        status_code=303
    )


@app.put("/books/{book_id}")
async def update_book(book_id: int, item: md.LivroUpdate):
    livro = db.collection.update_one(
        {"id": book_id},
        {"$set": item.model_dump()}
        )
    if livro.matched_count == 0:
        raise HTTPException(status_code=404, detail="Item not Found")
    
    return {"message": "Livro atualizado com sucesso!"}


@app.delete("/books/{book_id}")
async def delete_book(book_id: int):
    result = db.collection.delete_one({"id": book_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Book not Found")
    return {"message": "Deletado com sucesso"}
