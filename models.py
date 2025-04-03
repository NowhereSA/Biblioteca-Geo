from pydantic import BaseModel, Field
from bson import ObjectId
from typing import Optional, Annotated
from jinja2 import Environment, FileSystemLoader, PackageLoader, select_autoescape
from fastapi.templating import Jinja2Templates

#env = Environment(loader=FileSystemLoader('templates'))
#template = env.get_template(name="main.html")
templates = Jinja2Templates(directory="templates")  
class Biblioteca(BaseModel):
    titulo: str
    autor: str
    genero: str
    status: str
    descricao: str

class LivroUpdate(BaseModel):
    status: str