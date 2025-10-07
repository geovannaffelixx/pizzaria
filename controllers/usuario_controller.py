from fastapi import HTTPException
from sqlalchemy.orm import Session
from services.usuario import UsuarioService
from models.usuario import UsuarioCreate, UsuarioUpdate

class UsuarioController:
    def __init__(self):
        self.service = UsuarioService()

    def listar_usuarios(self, db: Session):
        return self.service.listar(db)

    def criar_usuario(self, usuario: UsuarioCreate, db: Session):
        return self.service.criar(usuario, db)

    def atualizar_usuario(self, usuario_id: int, dados: UsuarioUpdate, db: Session):
        u = self.service.atualizar(usuario_id, dados, db)
        if not u:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")
        return u

    def deletar_usuario(self, usuario_id: int, db: Session):
        u = self.service.deletar(usuario_id, db)
        if not u:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")
        return {"mensagem": f"Usuário {u.nome} removido com sucesso"}
