from sqlalchemy.orm import Session
from fastapi import HTTPException
from models.pedido import PedidoDB, PedidoCreate
from models.pizza import PizzaDB
from models.ingrediente import IngredienteDB

class PedidoController:
    def listar_pedidos(self, db: Session):
        return db.query(PedidoDB).all()

    def criar_pedido(self, pedido_data: PedidoCreate, usuario_id: int, tipo_usuario: str, db: Session):
        if tipo_usuario != "cliente":
            raise HTTPException(status_code=403, detail="Apenas clientes podem criar pedidos.")
        if not pedido_data.pizzas_ids:
            raise HTTPException(status_code=400, detail="O pedido deve conter pelo menos 1 pizza.")

        pizzas = db.query(PizzaDB).filter(PizzaDB.id.in_(pedido_data.pizzas_ids)).all()
        if not pizzas or len(pizzas) != len(pedido_data.pizzas_ids):
            raise HTTPException(status_code=404, detail="Pizza não encontrada.")

        extras = []
        if pedido_data.extras_ids:
            extras = db.query(IngredienteDB).filter(IngredienteDB.id.in_(pedido_data.extras_ids)).all()
            if len(extras) != len(pedido_data.extras_ids):
                raise HTTPException(status_code=404, detail="Ingrediente não encontrado.")

        total = sum(p.preco for p in pizzas) + sum(e.preco for e in extras)

        novo = PedidoDB(usuario_id=usuario_id, total=total)
        novo.pizzas = pizzas
        novo.extras = extras

        db.add(novo); db.commit(); db.refresh(novo)
        return novo
