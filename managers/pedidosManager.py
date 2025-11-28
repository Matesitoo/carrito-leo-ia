from managers.conexionManagerSupabase import ConexionManagerSupabase
from models.models import Pedido, PedidoCreate
from datetime import datetime

class PedidosManager:
    def __init__(self):
        self.supabase = ConexionManagerSupabase.get_client()
        self.table = 'pedidos'
    
    def crear_pedido(self, pedido: PedidoCreate):
        try:
            # Obtener el precio del producto
            producto_response = self.supabase.table('productos').select('precio').eq('id', pedido.producto_id).execute()
            
            if not producto_response.data:
                return {"data": None, "error": "Producto no encontrado"}
            
            precio = producto_response.data[0]['precio']
            total = precio * pedido.cantidad
            
            # Crear el pedido con el total calculado
            pedido_data = {
                'cliente_id': pedido.cliente_id,
                'producto_id': pedido.producto_id,
                'cantidad': pedido.cantidad,
                'total': total,
                'fecha': datetime.now().isoformat()
            }
            
            response = self.supabase.table(self.table).insert(pedido_data).execute()
            if response.data:
                return {"data": response.data[0], "error": None}
            return {"data": None, "error": "Error al crear pedido"}
        except Exception as e:
            return {"data": None, "error": str(e)}
    
    def obtener_pedidos(self):
        try:
            response = self.supabase.table(self.table).select('*, clientes(*), productos(*)').execute()
            return {"data": response.data, "error": None}
        except Exception as e:
            return {"data": None, "error": str(e)}
    
    def obtener_pedido(self, id: int):
        try:
            response = self.supabase.table(self.table).select('*, clientes(*), productos(*)').eq('id', id).execute()
            if response.data:
                return {"data": response.data[0], "error": None}
            return {"data": None, "error": "Pedido no encontrado"}
        except Exception as e:
            return {"data": None, "error": str(e)}
    
    def obtener_pedido_por_cliente(self, cliente_id: int):
        try:
            response = self.supabase.table(self.table).select('*, clientes(*), productos(*)').eq('cliente_id', cliente_id).execute()
            return {"data": response.data, "error": None}
        except Exception as e:
            return {"data": None, "error": str(e)}
    
    def total_por_pedido(self, pedido_id: int):
        try:
            response = self.supabase.table(self.table).select('total').eq('id', pedido_id).execute()
            if response.data:
                return {"data": response.data[0], "error": None}
            return {"data": None, "error": "Pedido no encontrado"}
        except Exception as e:
            return {"data": None, "error": str(e)}
    
    def filtrar_pedido_por_cliente(self, cliente_id: int):
        try:
            response = self.supabase.table(self.table).select('*, clientes(*), productos(*)').eq('cliente_id', cliente_id).execute()
            return {"data": response.data, "error": None}
        except Exception as e:
            return {"data": None, "error": str(e)}