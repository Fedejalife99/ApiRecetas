from pydantic import BaseModel
class Receta(BaseModel):
    id: int
    nombre: str
    ingredientes: list[str]
    pasos: list[str]
    categoria: str

class RecetaUpdate(BaseModel):
    nombre: str
    ingredientes: list[str]
    pasos: list[str]
    categoria: str