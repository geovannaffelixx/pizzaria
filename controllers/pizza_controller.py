from fastapi import HTTPException
from sqlalchemy.orm import Session
from services.pizza import PizzaService
from models.pizza import PizzaCreate, PizzaUpdate

class PizzaController:
    def __init__(self):
        self.service = PizzaService()

    def listar_pizzas(self, db: Session):
        return self.service.listar(db)

    def criar_pizza(self, pizza: PizzaCreate, db: Session):
        return self.service.criar(pizza, db)

    def atualizar_pizza(self, pizza_id: int, dados: PizzaUpdate, db: Session):
        pizza = self.service.atualizar(pizza_id, dados, db)
        if not pizza:
            raise HTTPException(status_code=404, detail="Pizza não encontrada")
        return pizza

    def deletar_pizza(self, pizza_id: int, db: Session):
        pizza = self.service.deletar(pizza_id, db)
        if not pizza:
            raise HTTPException(status_code=404, detail="Pizza não encontrada")
        return {"mensagem": f"Pizza {pizza.nome} removida com sucesso"}
