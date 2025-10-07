from sqlalchemy.orm import Session
from models.pizza import PizzaDB, PizzaCreate, PizzaUpdate
from fastapi import HTTPException

class PizzaController:
    def listar_pizzas(self, db: Session):
        return db.query(PizzaDB).all()

    def criar_pizza(self, pizza: PizzaCreate, db: Session):
        nova = PizzaDB(**pizza.model_dump())
        db.add(nova); db.commit(); db.refresh(nova)
        return nova

    def atualizar_pizza(self, pizza_id: int, dados: PizzaUpdate, db: Session):
        p = db.query(PizzaDB).filter(PizzaDB.id == pizza_id).first()
        if not p:
            raise HTTPException(status_code=404, detail="Pizza não encontrada")
        for k, v in dados.model_dump().items():
            setattr(p, k, v)
        db.commit(); db.refresh(p)
        return p

    def deletar_pizza(self, pizza_id: int, db: Session):
        p = db.query(PizzaDB).filter(PizzaDB.id == pizza_id).first()
        if not p:
            raise HTTPException(status_code=404, detail="Pizza não encontrada")
        db.delete(p); db.commit()
        return {"mensagem": f"Pizza {p.nome} removida com sucesso"}
