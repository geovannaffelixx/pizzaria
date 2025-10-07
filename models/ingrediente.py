from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Float
from database.config import Base

class IngredienteDB(Base):
    __tablename__ = "ingredientes"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    preco = Column(Float, nullable=False)

class Ingrediente(BaseModel):
    id: int
    nome: str
    preco: float
    class Config:
        from_attributes = True

class IngredienteCreate(BaseModel):
    nome: str
    preco: float
