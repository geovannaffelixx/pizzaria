from sqlalchemy.orm import Session
from models.usuario import UsuarioDB, UsuarioCreate, UsuarioUpdate

class UsuarioService:
    def listar(self, db: Session):
        return db.query(UsuarioDB).all()

    def criar(self, usuario: UsuarioCreate, db: Session):
        novo = UsuarioDB(nome=usuario.nome, tipo=usuario.tipo)
        db.add(novo)
        db.commit()
        db.refresh(novo)
        return novo

    def atualizar(self, usuario_id: int, dados: UsuarioUpdate, db: Session):
        u = db.query(UsuarioDB).filter(UsuarioDB.id == usuario_id).first()
        if not u:
            return None
        u.nome, u.tipo = dados.nome, dados.tipo
        db.commit()
        db.refresh(u)
        return u

    def deletar(self, usuario_id: int, db: Session):
        u = db.query(UsuarioDB).filter(UsuarioDB.id == usuario_id).first()
        if not u:
            return None
        db.delete(u)
        db.commit()
        return u
