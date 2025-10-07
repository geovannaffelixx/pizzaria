from sqlalchemy.orm import Session
from models.pedido import PedidoDB, PedidoCreate
from models.pizza import PizzaDB
from models.ingrediente import IngredienteDB

class PedidoService:
    def listar(self, db: Session):
        return db.query(PedidoDB).all()

    def criar(self, pedido_data: PedidoCreate, usuario_id: int, tipo_usuario: str, db: Session):
        if tipo_usuario != "cliente":
            return "forbidden"
        if not pedido_data.pizzas_ids:
            return "empty"

        pizzas = db.query(PizzaDB).filter(PizzaDB.id.in_(pedido_data.pizzas_ids)).all()
        if not pizzas or len(pizzas) != len(pedido_data.pizzas_ids):
            return "pizza_not_found"

        extras = []
        if pedido_data.extras_ids:
            extras = db.query(IngredienteDB).filter(IngredienteDB.id.in_(pedido_data.extras_ids)).all()
            if len(extras) != len(pedido_data.extras_ids):
                return "ingrediente_not_found"

        total = sum(p.preco for p in pizzas) + sum(e.preco for e in extras)
        novo = PedidoDB(usuario_id=usuario_id, total=total)
        novo.pizzas = pizzas
        novo.extras = extras
        db.add(novo)
        db.commit()
        db.refresh(novo)
        return novo
