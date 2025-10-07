from sqlalchemy.orm import Session
from models.usuario import UsuarioDB, UsuarioCreate, UsuarioUpdate
from fastapi import HTTPException

class UsuarioController:
    def listar_usuarios(self, db: Session):
        return db.query(UsuarioDB).all()

    def criar_usuario(self, usuario: UsuarioCreate, db: Session):
        novo = UsuarioDB(nome=usuario.nome, tipo=usuario.tipo)
        db.add(novo); db.commit(); db.refresh(novo)
        return novo

    def atualizar_usuario(self, usuario_id: int, dados: UsuarioUpdate, db: Session):
        u = db.query(UsuarioDB).filter(UsuarioDB.id == usuario_id).first()
        if not u:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")
        u.nome, u.tipo = dados.nome, dados.tipo
        db.commit(); db.refresh(u)
        return u

    def deletar_usuario(self, usuario_id: int, db: Session):
        u = db.query(UsuarioDB).filter(UsuarioDB.id == usuario_id).first()
        if not u:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")
        db.delete(u); db.commit()
        return {"mensagem": f"Usuário {u.nome} removido com sucesso"}
