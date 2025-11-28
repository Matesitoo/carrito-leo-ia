from fastapi import APIRouter, HTTPException
from models.models import Producto
from managers.productosManager import ProductosManager

router = APIRouter()
manager = ProductosManager()

@router.get("/obtener_productos")
async def obtener_productos():
    result = manager.obtener_productos()
    if result["error"]:
        raise HTTPException(status_code=400, detail=result["error"])
    return result["data"]

@router.post("/crear_productos")
async def crear_productos(producto: Producto):
    result = manager.crear_producto(producto)
    if result["error"]:
        raise HTTPException(status_code=400, detail=result["error"])
    return result["data"]

@router.put("/modificar_producto/{id}")
async def modificar_producto(id: int, producto: Producto):
    result = manager.modificar_producto(id, producto)
    if result["error"]:
        raise HTTPException(status_code=400, detail=result["error"])
    return result["data"]

@router.delete("/eliminar_producto/{id}")
async def eliminar_producto(id: int):
    result = manager.eliminar_producto(id)
    if result["error"]:
        raise HTTPException(status_code=400, detail=result["error"])
    return result["data"]