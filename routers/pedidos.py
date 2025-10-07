from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.config import get_db
from controllers.pedido_controller import PedidoController
from models.pedido import PedidoCreate, Pedido
from JWT.auth import obter_usuario_atual

router = APIRouter(prefix="/pedidos", tags=["Pedidos"])
controller = PedidoController()

@router.post("/", response_model=Pedido)
def criar_pedido(pedido: PedidoCreate, db: Session = Depends(get_db), usuario_atual=Depends(obter_usuario_atual)):
    return controller.criar_pedido(pedido, usuario_atual["id"], usuario_atual["tipo"], db)

@router.get("/", response_model=list[Pedido])
def listar_pedidos(db: Session = Depends(get_db)):
    return controller.listar_pedidos(db)
