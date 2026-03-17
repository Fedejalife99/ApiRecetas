import sys
import os

# Add the parent directory of this file's directory (i.e., the first ApiRecetas folder) to sys.path
# so that absolute imports like `from Api.Recetas` work when running this file directly.
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import json
from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from Api.gestionBd.database import engine, get_db, Base
from Api.gestionBd.models import RecetaModel
from Api.Recetas import Recetas
from Api.Receta import Receta, RecetaUpdate
from fastapi import Query

app = FastAPI()
Base.metadata.create_all(bind=engine)
recetas = Recetas()
@app.get("/")
def inicio():
    return {"mensaje": "API de recetas funcionando"}


@app.post("/recetas", status_code=201)
def crear_receta(receta: Receta, db: Session = Depends(get_db)):
    existing = db.query(RecetaModel).filter(RecetaModel.nombre.ilike(f"%{receta.nombre}%")).all()
    if existing:
        raise HTTPException(status_code=400, detail="Ya existe una receta con ese nombre")
    nueva = RecetaModel(
        nombre=receta.nombre,
        ingredientes=json.dumps(receta.ingredientes, ensure_ascii=False),
        pasos=json.dumps(receta.pasos, ensure_ascii=False),
    )
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return {"mensaje": "Receta creada exitosamente", "id": nueva.id}

@app.get("/recetas")
def mostrar_recetas(db: Session = Depends(get_db)):
    return [_model_to_dict(r) for r in db.query(RecetaModel).all()]

@app.delete("/recetas/{nombre}")
def eliminar_receta(nombre: str, db: Session = Depends(get_db)):
    receta = db.query(RecetaModel).filter(RecetaModel.nombre == nombre).first()
    if not receta:
        raise HTTPException(status_code=404, detail="Receta no encontrada")
    db.delete(receta)
    db.commit()
    return {"mensaje": "Receta eliminada exitosamente"}

@app.get("/recetas/coincidentes")
def recetas_coincidentes(
    ingredientes: list[str] = Query(...),
    db: Session = Depends(get_db),
):
    todas = db.query(RecetaModel).all()
    resultado = []
    for receta in todas:
        lista_ingredientes = json.loads(receta.ingredientes)
        if any(ing in lista_ingredientes for ing in ingredientes):
            resultado.append(_model_to_dict(receta))
    return resultado


@app.put("/recetas/{nombre}")
    #obtener la receta por nombre
    #recibir parametros para actualizar
    #ignorar si el nombre de la receta esta escrito exactamente igual
    #si la receta no existe muestro error 404
    #si existe actualizo los campos ingresados
    #guardo en la base de datos
    #retorno un mensaje de exito
@app.put("/recetas/{nombre}")
def actualizar_receta(nombre: str, receta_nueva: RecetaUpdate, db: Session = Depends(get_db)):  
    receta = db.query(RecetaModel).filter(RecetaModel.nombre.ilike(f"%{nombre}%")).first()
    if not receta:
        raise HTTPException(status_code=404, detail="Receta no encontrada")
    receta.nombre = receta_nueva.nombre
    receta.ingredientes = json.dumps(receta_nueva.ingredientes, ensure_ascii=False)
    receta.pasos = json.dumps(receta_nueva.pasos, ensure_ascii=False)
    db.commit()
    db.refresh(receta)
    return {"mensaje": "Receta actualizada exitosamente"}
    
#obtengo id 
#si no existe una receta con dicho id muestro error 404
#si existe retorno la receta
@app.get("/recetas/{id}")
def mostrar_receta(id: int, db: Session = Depends(get_db)):
    receta = db.query(RecetaModel).filter(RecetaModel.id == id).first()
    if not receta:
        return []
    return _model_to_dict(receta)

#si no recibo parametros seteo skip en 0 y limit en 10
@app.get("/recetas")
def mostrar_recetas_limitadas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    recetas = db.query(RecetaModel).offset(skip).limit(limit).all()
    return [_model_to_dict(r) for r in recetas]

#obtengo categoria
#si la categoria no existe  muestro error 404
#si existe retorno las recetas que tengan esa categoria
@app.get("/recetas/categoria/{categoria}")
def mostrar_recetas_por_categoria(categoria: str, db: Session = Depends(get_db)):
    recetas = db.query(RecetaModel).filter(RecetaModel.categoria == categoria).all()
    if not recetas:
        return []
    return [_model_to_dict(r) for r in recetas]



def _model_to_dict(r: RecetaModel) -> dict:
    ingredientes = []
    for ri in r.ingredientes:
        ingredientes.append({
            "nombre": ri.ingrediente.nombre,
            "cantidad": ri.cantidad,
            "unidad": ri.unidad
        })

    return {
        "id": r.id,
        "nombre": r.nombre,
        "categoria": r.categoria,
        "ingredientes": ingredientes,
        "pasos": json.loads(r.pasos)
    }

