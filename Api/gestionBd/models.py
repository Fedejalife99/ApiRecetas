# Api/models.py
from sqlalchemy import Column, Integer, String, Text, ForeignKey, Float
from sqlalchemy.orm import relationship
from Api.gestionBd.database import Base


class IngredienteModel(Base):
    __tablename__ = "ingredientes"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(100), nullable=False, unique=True, index=True)

class RecetaModel(Base):
    __tablename__ = "recetas"

    id         = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre     = Column(String(100), nullable=False, unique=True, index=True)
    pasos        = Column(Text, nullable=False)
    categoria = Column(String(50), nullable=False)
    ingredientes = relationship("RecetaIngrediente", back_populates="receta")
    imagen = Column(String(200), nullable=True)  # nullable porque no todas tienen imagen



class RecetaIngrediente(Base):
    __tablename__ = "receta_ingrediente"
    receta_id = Column(Integer, ForeignKey("recetas.id"), primary_key=True)
    ingrediente_id = Column(Integer, ForeignKey("ingredientes.id"), primary_key=True)
    cantidad = Column(Float, nullable=False)
    unidad = Column(String(50), nullable=False)
    receta      = relationship("RecetaModel", back_populates="ingredientes")
    ingrediente = relationship("IngredienteModel")
