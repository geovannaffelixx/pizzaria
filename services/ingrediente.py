from sqlalchemy.orm import Session
from models.ingrediente import IngredienteDB, IngredienteCreate

class IngredienteService:
    def listar(self, db: Session):
        return db.query(IngredienteDB).all()

    def criar(self, ingrediente: IngredienteCreate, db: Session):
        novo = IngredienteDB(**ingrediente.model_dump())
        db.add(novo)
        db.commit()
        db.refresh(novo)
        return novo

    def atualizar(self, ingrediente_id: int, ingrediente: IngredienteCreate, db: Session):
        ingr = db.query(IngredienteDB).filter(IngredienteDB.id == ingrediente_id).first()
        if not ingr:
            return None
        ingr.nome = ingrediente.nome
        ingr.preco = ingrediente.preco
        db.commit()
        db.refresh(ingr)
        return ingr

    def deletar(self, ingrediente_id: int, db: Session):
        ing = db.query(IngredienteDB).filter(IngredienteDB.id == ingrediente_id).first()
        if not ing:
            return None
        db.delete(ing)
        db.commit()
        return ing
