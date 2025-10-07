from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.config import get_db
from controllers.ingrediente_controller import IngredienteController
from models.ingrediente import Ingrediente, IngredienteCreate

router = APIRouter(prefix="/ingredientes", tags=["Ingredientes"])
controller = IngredienteController()

@router.get("/", response_model=list[Ingrediente])
def listar_ingredientes(db: Session = Depends(get_db)):
    return controller.listar_ingredientes(db)

@router.post("/", response_model=Ingrediente)
def criar_ingrediente(ingrediente: IngredienteCreate, db: Session = Depends(get_db)):
    return controller.criar_ingrediente(ingrediente, db)

@router.put("/{ingrediente_id}", response_model=Ingrediente)
def atualizar_ingrediente(ingrediente_id: int, ingrediente: IngredienteCreate, db: Session = Depends(get_db)):
    return controller.atualizar_ingrediente(ingrediente_id, ingrediente, db)

@router.delete("/{ingrediente_id}")
def deletar_ingrediente(ingrediente_id: int, db: Session = Depends(get_db)):
    return controller.deletar_ingrediente(ingrediente_id, db)
