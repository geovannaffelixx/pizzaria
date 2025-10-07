from pydantic import BaseModel
from sqlalchemy import Column, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from database.config import Base
from models.pizza import PizzaDB, Pizza
from models.ingrediente import IngredienteDB, Ingrediente

pedido_pizza = Table(
    "pedido_pizza",
    Base.metadata,
    Column("pedido_id", Integer, ForeignKey("pedidos.id")),
    Column("pizza_id", Integer, ForeignKey("pizzas.id")),
)

pedido_ingrediente = Table(
    "pedido_ingrediente",
    Base.metadata,
    Column("pedido_id", Integer, ForeignKey("pedidos.id")),
    Column("ingrediente_id", Integer, ForeignKey("ingredientes.id")),
)

class PedidoDB(Base):
    __tablename__ = "pedidos"
    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    total = Column(Float, nullable=False)

    pizzas = relationship("PizzaDB", secondary=pedido_pizza)
    extras = relationship("IngredienteDB", secondary=pedido_ingrediente)

class Pedido(BaseModel):
    id: int
    usuario_id: int
    total: float
    pizzas: list[Pizza]
    extras: list[Ingrediente] = []
    class Config:
        from_attributes = True

class PedidoCreate(BaseModel):
    pizzas_ids: list[int]
    extras_ids: list[int] = []
