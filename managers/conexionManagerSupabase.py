import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

class ConexionManagerSupabase:
    _instance = None
    
    def __init__(self):
        if ConexionManagerSupabase._instance is not None:
            raise Exception("Esta clase es un Singleton!")
        else:
            self.url = os.getenv('SUPABASE_URL')
            self.key = os.getenv('SUPABASE_KEY')
            if not self.url or not self.key:
                self.url = "https://placeholder.supabase.co"
                self.key = "placeholder"
            else:
                self.client: Client = create_client(self.url, self.key)
            ConexionManagerSupabase._instance = self
    
    @staticmethod
    def get_client():
        if ConexionManagerSupabase._instance is None:
            ConexionManagerSupabase()
        return ConexionManagerSupabase._instance.client