from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models.usuario import UsuarioDB
from database.config import get_db
from JWT.auth import criar_token

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login")
def login(nome: str, tipo: str, db: Session = Depends(get_db)):
    usuario = db.query(UsuarioDB).filter(UsuarioDB.nome == nome, UsuarioDB.tipo == tipo).first()
    if not usuario:
        raise HTTPException(status_code=401, detail="Usuário não encontrado ou tipo incorreto")
    token = criar_token(usuario.id, usuario.nome, usuario.tipo)
    return {"token": token}
