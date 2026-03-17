import sys
import os

# Add the parent directory of this file's directory (i.e., the first ApiRecetas folder) to sys.path
# so that absolute imports like `from Api.Recetas` work when running this file directly.
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI
from Api.Recetas import Recetas
from Api.Receta import Receta
from fastapi import Query
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

@app.delete("/recetas/{nombre}")
def eliminar_receta(nombre: str):
    recetas.eliminar_receta(nombre)
    return {"mensaje": "Receta eliminada exitosamente"}

@app.get("/recetas/coincidentes")
def recetas_coincidentes(ingredientes: list[str] = Query()):
    return recetas.recetasCoinciden(ingredientes)
