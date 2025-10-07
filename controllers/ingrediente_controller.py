from sqlalchemy.orm import Session
from models.ingrediente import IngredienteDB, IngredienteCreate
from fastapi import HTTPException

class IngredienteController:
    def listar_ingredientes(self, db: Session):
        return db.query(IngredienteDB).all()

    def criar_ingrediente(self, ingrediente: IngredienteCreate, db: Session):
        novo = IngredienteDB(**ingrediente.model_dump())
        db.add(novo); db.commit(); db.refresh(novo)
        return novo

    def atualizar_ingrediente(self, ingrediente_id: int, ingrediente: IngredienteCreate, db: Session):
        ingr = db.query(IngredienteDB).filter(IngredienteDB.id == ingrediente_id).first()
        if not ingr:
            raise HTTPException(status_code=404, detail="Ingrediente não encontrado")
        ingr.nome = ingrediente.nome
        ingr.preco = ingrediente.preco
        db.commit(); db.refresh(ingr)
        return ingr

    def deletar_ingrediente(self, ingrediente_id: int, db: Session):
        ing = db.query(IngredienteDB).filter(IngredienteDB.id == ingrediente_id).first()
        if not ing:
            raise HTTPException(status_code=404, detail="Ingrediente não encontrado")
        db.delete(ing); db.commit()
        return {"mensagem": f"Ingrediente '{ing.nome}' removido com sucesso"}
