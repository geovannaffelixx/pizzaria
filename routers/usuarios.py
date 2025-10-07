from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.usuario import Usuario, UsuarioCreate, UsuarioUpdate
from database.config import get_db
from controllers.usuario_controller import UsuarioController

router = APIRouter(prefix="/usuarios", tags=["Usuários"])
controller = UsuarioController()

@router.get("/", response_model=list[Usuario])
def listar_usuarios(db: Session = Depends(get_db)):
    return controller.listar_usuarios(db)

@router.post("/", response_model=Usuario)
def criar_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    return controller.criar_usuario(usuario, db)

@router.put("/{usuario_id}", response_model=Usuario)
def atualizar_usuario(usuario_id: int, dados: UsuarioUpdate, db: Session = Depends(get_db)):
    return controller.atualizar_usuario(usuario_id, dados, db)

@router.delete("/{usuario_id}")
def deletar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    return controller.deletar_usuario(usuario_id, db)
