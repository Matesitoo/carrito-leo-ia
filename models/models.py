from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Cliente(BaseModel):
    id: Optional[int] = None
    nombre: str
    email: str
    telefono: Optional[str] = None

class Producto(BaseModel):
    id: Optional[int] = None
    nombre: str
    precio: float
    stock: int

class Pedido(BaseModel):
    id: Optional[int] = None
    cliente_id: int
    producto_id: int
    cantidad: int
    total: Optional[float] = None
    fecha: Optional[str] = None

class PedidoCreate(BaseModel):
    cliente_id: int
    producto_id: int
    cantidad: int