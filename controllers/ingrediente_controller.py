from fastapi import HTTPException
from sqlalchemy.orm import Session
from services.ingrediente import IngredienteService
from models.ingrediente import IngredienteCreate

class IngredienteController:
    def __init__(self):
        self.service = IngredienteService()

    def listar_ingredientes(self, db: Session):
        return self.service.listar(db)

    def criar_ingrediente(self, ingrediente: IngredienteCreate, db: Session):
        return self.service.criar(ingrediente, db)

    def atualizar_ingrediente(self, ingrediente_id: int, ingrediente: IngredienteCreate, db: Session):
        ingr = self.service.atualizar(ingrediente_id, ingrediente, db)
        if not ingr:
            raise HTTPException(status_code=404, detail="Ingrediente não encontrado")
        return ingr

    def deletar_ingrediente(self, ingrediente_id: int, db: Session):
        ing = self.service.deletar(ingrediente_id, db)
        if not ing:
            raise HTTPException(status_code=404, detail="Ingrediente não encontrado")
        return {"mensagem": f"Ingrediente '{ing.nome}' removido com sucesso"}
