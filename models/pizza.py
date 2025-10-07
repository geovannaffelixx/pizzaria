from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Float
from database.config import Base

class PizzaDB(Base):
    __tablename__ = "pizzas"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    ingredientes = Column(String, nullable=False)
    preco = Column(Float, nullable=False)
    tamanho = Column(String, nullable=False)

class Pizza(BaseModel):
    id: int
    nome: str
    ingredientes: str
    preco: float
    tamanho: str
    class Config:
        from_attributes = True

class PizzaCreate(BaseModel):
    nome: str
    ingredientes: str
    preco: float
    tamanho: str

class PizzaUpdate(BaseModel):
    nome: str
    ingredientes: str
    preco: float
    tamanho: str
