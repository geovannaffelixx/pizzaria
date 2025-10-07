from sqlalchemy.orm import Session
from models.pizza import PizzaDB, PizzaCreate, PizzaUpdate

class PizzaService:
    def listar(self, db: Session):
        return db.query(PizzaDB).all()

    def criar(self, pizza: PizzaCreate, db: Session):
        nova = PizzaDB(**pizza.model_dump())
        db.add(nova)
        db.commit()
        db.refresh(nova)
        return nova

    def atualizar(self, pizza_id: int, dados: PizzaUpdate, db: Session):
        p = db.query(PizzaDB).filter(PizzaDB.id == pizza_id).first()
        if not p:
            return None
        for k, v in dados.model_dump().items():
            setattr(p, k, v)
        db.commit()
        db.refresh(p)
        return p

    def deletar(self, pizza_id: int, db: Session):
        p = db.query(PizzaDB).filter(PizzaDB.id == pizza_id).first()
        if not p:
            return None
        db.delete(p)
        db.commit()
        return p
