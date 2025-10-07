from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.pizza import Pizza, PizzaCreate, PizzaUpdate
from database.config import get_db
from controllers.pizza_controller import PizzaController
from JWT.auth import obter_usuario_atual

router = APIRouter(prefix="/pizzas", tags=["Pizzas"])
controller = PizzaController()

@router.get("/", response_model=list[Pizza])
def listar_pizzas(db: Session = Depends(get_db)):
    return controller.listar_pizzas(db)

@router.post("/", response_model=Pizza)
def criar_pizza(pizza: PizzaCreate, db: Session = Depends(get_db), usuario=Depends(obter_usuario_atual)):
    if usuario["tipo"] != "funcionario":
        raise HTTPException(status_code=403, detail="Apenas funcionários podem cadastrar pizzas")
    return controller.criar_pizza(pizza, db)

@router.put("/{pizza_id}", response_model=Pizza)
def atualizar_pizza(pizza_id: int, dados: PizzaUpdate, db: Session = Depends(get_db), usuario=Depends(obter_usuario_atual)):
    if usuario["tipo"] != "funcionario":
        raise HTTPException(status_code=403, detail="Apenas funcionários podem editar pizzas")
    return controller.atualizar_pizza(pizza_id, dados, db)

@router.delete("/{pizza_id}")
def deletar_pizza(pizza_id: int, db: Session = Depends(get_db), usuario=Depends(obter_usuario_atual)):
    if usuario["tipo"] != "funcionario":
        raise HTTPException(status_code=403, detail="Apenas funcionários podem excluir pizzas")
    return controller.deletar_pizza(pizza_id, db)
