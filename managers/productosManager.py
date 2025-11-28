from managers.conexionManagerSupabase import ConexionManagerSupabase
from models.models import Producto

class ProductosManager:
    def __init__(self):
        self.supabase = ConexionManagerSupabase.get_client()
        self.table = 'productos'
    
    def obtener_productos(self):
        try:
            response = self.supabase.table(self.table).select('*').execute()
            return {"data": response.data, "error": None}
        except Exception as e:
            return {"data": None, "error": str(e)}
    
    def crear_producto(self, producto: Producto):
        try:
            response = self.supabase.table(self.table).insert(producto.dict(exclude={'id'})).execute()
            if response.data:
                return {"data": response.data[0], "error": None}
            return {"data": None, "error": "Error al crear producto"}
        except Exception as e:
            return {"data": None, "error": str(e)}
    
    def modificar_producto(self, id: int, producto: Producto):
        try:
            producto_data = producto.dict(exclude={'id'})
            response = self.supabase.table(self.table).update(producto_data).eq('id', id).execute()
            if response.data:
                return {"data": response.data[0], "error": None}
            return {"data": None, "error": "Producto no encontrado"}
        except Exception as e:
            return {"data": None, "error": str(e)}
    
    def eliminar_producto(self, id: int):
        try:
            response = self.supabase.table(self.table).delete().eq('id', id).execute()
            return {"data": {"message": "Producto eliminado correctamente"}, "error": None}
        except Exception as e:
            return {"data": None, "error": str(e)}