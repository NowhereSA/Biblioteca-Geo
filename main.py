from fastapi import FastAPI, Form
from pydantic import BaseModel
from jinja2 import Environment, FileSystemLoader, PackageLoader, select_autoescape
from pymongo import MongoClient
#from typing import Annotated

env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template(name="main.html")
app = FastAPI()
cliente = MongoClient('mongodb://localhost:27017')
db = cliente['Biblioteca']
collection = db['dados']

# título, autor, ano de publicação, gênero e status
# Modelagem

class Biblioteca(BaseModel):
    id: int
    titulo: str
    autor: str
    genero: str
    status: str

@app.get("/")
async def main():
    return "Hello World"

@app.get("/books")
async def show_book():
    books = list(collection.find({}, {"_id": 0})) # Id zero é para excluir todos ids (filtro)
    return books

@app.post("/books")
#async def add_book(data: Annotated[Biblioteca, Form()]):
async def add_book(data: Biblioteca):
    collection.insert_one(data.model_dump())
    return {"message": "Deu certo"}

@app.put("/books/{book_id}")
async def update_book(book_id: int):
    print(book_id)
    livro = collection.find_one({"id": book_id}, {"_id": 0})
    print(livro)
    return livro
"""
@app.delete("/books/{book_id}")
async def delete_book():
    return {"message": "Nothing"}
"""
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)