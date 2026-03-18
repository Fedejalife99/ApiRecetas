import sys
import os

# Add the parent directory of this file's directory (i.e., the first ApiRecetas folder) to sys.path
# so that absolute imports like `from Api.Recetas` work when running this file directly.
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import json
from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from Api.gestionBd.database import engine, get_db, Base
from Api.gestionBd.models import RecetaModel, IngredienteModel, RecetaIngrediente
from Api.Receta import Receta, RecetaUpdate, Ingrediente
from fastapi import Query,UploadFile, File
from Api.middleware import http_exception_handler, generic_exception_handler
from fastapi.staticfiles import StaticFiles
import os

# crear la carpeta si no existe
os.makedirs("imagenes", exist_ok=True)



app = FastAPI()
# servir la carpeta como archivos estáticos
app.mount("/imagenes", StaticFiles(directory="imagenes"), name="imagenes")
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(Exception, generic_exception_handler)

Base.metadata.create_all(bind=engine)


def _model_to_dict(r: RecetaModel) -> dict:
    ingredientes = []
    for ri in r.ingredientes:
        ingredientes.append({
            "nombre": ri.ingrediente.nombre,
            "cantidad": ri.cantidad,
            "unidad": ri.unidad,
        })

    return {
        "id": r.id,
        "nombre": r.nombre,
        "categoria": r.categoria,
        "ingredientes": ingredientes,
        "pasos": json.loads(r.pasos),
        "imagen": r.imagen
    }


@app.get("/")
def inicio():
    return {"mensaje": "API de recetas funcionando"}


@app.post("/recetas", status_code=201)
def crear_receta(receta: Receta, db: Session = Depends(get_db)):
    # verificar que no exista
    existing = db.query(RecetaModel).filter(RecetaModel.nombre.ilike(f"%{receta.nombre}%")).first()
    if existing:
        raise HTTPException(status_code=400, detail="Ya existe una receta con ese nombre")

    # crear la receta
    nueva = RecetaModel(
        nombre=receta.nombre,
        categoria=receta.categoria,
        pasos=json.dumps(receta.pasos, ensure_ascii=False),
    )
    db.add(nueva)
    db.flush()

    # crear ingredientes y asociaciones
    for ing in receta.ingredientes:
        ingrediente = db.query(IngredienteModel).filter(
            IngredienteModel.nombre == ing.nombre
        ).first()

        if not ingrediente:
            ingrediente = IngredienteModel(nombre=ing.nombre)
            db.add(ingrediente)
            db.flush()

        asociacion = RecetaIngrediente(
            receta_id=nueva.id,
            ingrediente_id=ingrediente.id,
            cantidad=ing.cantidad,
            unidad=ing.unidad,
        )
        db.add(asociacion)

    db.commit()
    db.refresh(nueva)
    return {"mensaje": "Receta creada exitosamente", "id": nueva.id}
#si no recibo parametros seteo skip en 0 y limit en 10
@app.get("/recetas/limitadas")
def mostrar_recetas_limitadas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    recetas = db.query(RecetaModel).offset(skip).limit(limit).all()
    return [_model_to_dict(r) for r in recetas]

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
        for ri in receta.ingredientes:
            if ri.ingrediente.nombre in ingredientes:
                resultado.append(_model_to_dict(receta))
                break
    return resultado



@app.put("/recetas/{nombre}")
def actualizar_receta(nombre: str, receta_nueva: RecetaUpdate, db: Session = Depends(get_db)):  
    receta = db.query(RecetaModel).filter(RecetaModel.nombre.ilike(f"%{nombre}%")).first()
    if not receta:
        raise HTTPException(status_code=404, detail="Receta no encontrada")
    receta.nombre = receta_nueva.nombre
    receta.pasos = json.dumps(receta_nueva.pasos, ensure_ascii=False)
    receta.categoria = receta_nueva.categoria
    db.query(RecetaIngrediente).filter(RecetaIngrediente.receta_id == receta.id).delete()
    # crear ingredientes y asociaciones
    for ing in receta_nueva.ingredientes:
        ingrediente = db.query(IngredienteModel).filter(
            IngredienteModel.nombre == ing.nombre
        ).first()

        if not ingrediente:
            ingrediente = IngredienteModel(nombre=ing.nombre)
            db.add(ingrediente)
            db.flush()

        asociacion = RecetaIngrediente(
            receta_id=receta.id,
            ingrediente_id=ingrediente.id,
            cantidad=ing.cantidad,
            unidad=ing.unidad,
        )
        db.add(asociacion)
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


#obtengo categoria
#si la categoria no existe  muestro error 404
#si existe retorno las recetas que tengan esa categoria
@app.get("/recetas/categoria/{categoria}")
def mostrar_recetas_por_categoria(categoria: str, db: Session = Depends(get_db)):
    recetas = db.query(RecetaModel).filter(RecetaModel.categoria == categoria).all()
    if not recetas:
        return []
    return [_model_to_dict(r) for r in recetas]

@app.post("/recetas/{id}/imagen")
async def subir_imagen(id: int, imagen: UploadFile = File(...), db: Session = Depends(get_db)):
    receta = db.query(RecetaModel).filter(RecetaModel.id == id).first()
    if not receta:
        raise HTTPException(status_code=404, detail="Receta no encontrada")

    # guardar el archivo
    ruta = f"imagenes/{id}_{imagen.filename}"
    with open(ruta, "wb") as f:
        f.write(await imagen.read())

    # guardar la ruta en la BD
    receta.imagen = ruta
    db.commit()
    return {"mensaje": "Imagen subida exitosamente", "ruta": ruta}




