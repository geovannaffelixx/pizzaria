from fastapi import HTTPException
from sqlalchemy.orm import Session
from services.pedido import PedidoService
from models.pedido import PedidoCreate

class PedidoController:
    def __init__(self):
        self.service = PedidoService()

    def listar_pedidos(self, db: Session):
        return self.service.listar(db)

    def criar_pedido(self, pedido_data: PedidoCreate, usuario_id: int, tipo_usuario: str, db: Session):
        result = self.service.criar(pedido_data, usuario_id, tipo_usuario, db)
        if result == "forbidden":
            raise HTTPException(status_code=403, detail="Apenas clientes podem criar pedidos.")
        if result == "empty":
            raise HTTPException(status_code=400, detail="O pedido deve conter pelo menos 1 pizza.")
        if result == "pizza_not_found":
            raise HTTPException(status_code=404, detail="Pizza não encontrada.")
        if result == "ingrediente_not_found":
            raise HTTPException(status_code=404, detail="Ingrediente não encontrado.")
        return result
