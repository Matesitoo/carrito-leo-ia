from fastapi import APIRouter, HTTPException
from models.models import Cliente
from managers.clientesManager import ClientesManager

router = APIRouter()
manager = ClientesManager()

@router.get("/obtener_clientes")
async def obtener_clientes():
    result = manager.obtener_clientes()
    if result["error"]:
        raise HTTPException(status_code=400, detail=result["error"])
    return result["data"]

@router.get("/obtener_cliente/{id}")
async def obtener_cliente(id: int):
    result = manager.obtener_cliente(id)
    if result["error"]:
        raise HTTPException(status_code=404, detail=result["error"])
    return result["data"]

@router.put("/modificar_cliente/{id}")
async def modificar_cliente(id: int, cliente: Cliente):
    result = manager.modificar_cliente(id, cliente)
    if result["error"]:
        raise HTTPException(status_code=400, detail=result["error"])
    return result["data"]

@router.delete("/eliminar_cliente/{id}")
async def eliminar_cliente(id: int):
    result = manager.eliminar_cliente(id)
    if result["error"]:
        raise HTTPException(status_code=400, detail=result["error"])
    return result["data"]

@router.post("/crear_cliente")
async def crear_cliente(cliente: Cliente):
    result = manager.crear_cliente(cliente)
    if result["error"]:
        raise HTTPException(status_code=400, detail=result["error"])
    return result["data"]