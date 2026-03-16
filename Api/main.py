from fastapi import FastAPI
from Recetas import Recetas
from Receta import Receta
app = FastAPI()
recetas = Recetas()
@app.get("/")
def inicio():
    return {"mensaje": "API de recetas funcionando"}


@app.post("/recetas")
def crear_receta(receta: Receta):
    recetas.agregar_receta(receta)
    return {"mensaje": "Receta creada exitosamente"}

@app.get("/recetas")
def mostrar_recetas():
    return recetas.mostrar_recetas()