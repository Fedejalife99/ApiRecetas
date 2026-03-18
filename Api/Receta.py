from pydantic import BaseModel

class Ingrediente(BaseModel):
    nombre: str
    cantidad: float
    unidad: str
    
class Receta(BaseModel):
    nombre: str
    ingredientes: list[Ingrediente]
    pasos: list[str]
    categoria: str

class RecetaUpdate(BaseModel):
    nombre: str
    ingredientes: list[Ingrediente]
    pasos: list[str]
    categoria: str


