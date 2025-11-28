from managers.conexionManagerSupabase import ConexionManagerSupabase
from models.models import Cliente

class ClientesManager:
    def __init__(self):
        self.supabase = ConexionManagerSupabase.get_client()
        self.table = 'clientes'
    
    def obtener_clientes(self):
        try:
            response = self.supabase.table(self.table).select('*').execute()
            return {"data": response.data, "error": None}
        except Exception as e:
            return {"data": None, "error": str(e)}
    
    def obtener_cliente(self, id: int):
        try:
            response = self.supabase.table(self.table).select('*').eq('id', id).execute()
            if response.data:
                return {"data": response.data[0], "error": None}
            return {"data": None, "error": "Cliente no encontrado"}
        except Exception as e:
            return {"data": None, "error": str(e)}
    
    def modificar_cliente(self, id: int, cliente: Cliente):
        try:
            # Remover el id del diccionario para evitar conflictos
            cliente_data = cliente.dict(exclude={'id'})
            response = self.supabase.table(self.table).update(cliente_data).eq('id', id).execute()
            if response.data:
                return {"data": response.data[0], "error": None}
            return {"data": None, "error": "Cliente no encontrado"}
        except Exception as e:
            return {"data": None, "error": str(e)}
    
    def eliminar_cliente(self, id: int):
        try:
            response = self.supabase.table(self.table).delete().eq('id', id).execute()
            return {"data": {"message": "Cliente eliminado correctamente"}, "error": None}
        except Exception as e:
            return {"data": None, "error": str(e)}
    
    def crear_cliente(self, cliente: Cliente):
        try:
            response = self.supabase.table(self.table).insert(cliente.dict(exclude={'id'})).execute()
            if response.data:
                return {"data": response.data[0], "error": None}
            return {"data": None, "error": "Error al crear cliente"}
        except Exception as e:
            return {"data": None, "error": str(e)}