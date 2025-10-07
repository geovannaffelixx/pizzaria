from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from database.config import Base

class UsuarioDB(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    tipo = Column(String, nullable=False) 
    
class Usuario(BaseModel):
    id: int
    nome: str
    tipo: str
    class Config:
        from_attributes = True

class UsuarioCreate(BaseModel):
    nome: str
    tipo: str

class UsuarioUpdate(BaseModel):
    nome: str
    tipo: str
