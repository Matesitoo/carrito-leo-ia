from fastapi import APIRouter, HTTPException
from models.models import PedidoCreate
from managers.pedidosManager import PedidosManager

router = APIRouter()
manager = PedidosManager()

@router.post("/crear_pedido")
async def crear_pedido(pedido: PedidoCreate):
    result = manager.crear_pedido(pedido)
    if result["error"]:
        raise HTTPException(status_code=400, detail=result["error"])
    return result["data"]

@router.get("/obtener_pedidos")
async def obtener_pedidos():
    result = manager.obtener_pedidos()
    if result["error"]:
        raise HTTPException(status_code=400, detail=result["error"])
    return result["data"]

@router.get("/obtener_pedido/{id}")
async def obtener_pedido(id: int):
    result = manager.obtener_pedido(id)
    if result["error"]:
        raise HTTPException(status_code=404, detail=result["error"])
    return result["data"]

@router.get("/obtener_pedido_por_cliente/{cliente_id}")
async def obtener_pedido_por_cliente(cliente_id: int):
    result = manager.obtener_pedido_por_cliente(cliente_id)
    if result["error"]:
        raise HTTPException(status_code=400, detail=result["error"])
    return result["data"]

@router.get("/total_por_pedido/{pedido_id}")
async def total_por_pedido(pedido_id: int):
    result = manager.total_por_pedido(pedido_id)
    if result["error"]:
        raise HTTPException(status_code=404, detail=result["error"])
    return result["data"]

@router.get("/filtrar_pedido_por_cliente/{cliente_id}")
async def filtrar_pedido_por_cliente(cliente_id: int):
    result = manager.filtrar_pedido_por_cliente(cliente_id)
    if result["error"]:
        raise HTTPException(status_code=400, detail=result["error"])
    return result["data"]