from ..repositories import LocalRepository
from ..schemas import Local, LocalCreate, LocalUpdate
from psycopg2.errors import RaiseException

class LocalController:
    """
    Clase que contiene la lógica para manejar las peticiones para locales.    
    """
    def __init__(self, db_cursor):
        # El cursor se usa para instanciar el Repository.
        self.repository = LocalRepository(db_cursor)

    def create_local(self, local: LocalCreate):
        try:            
            data = self.repository.create_local(local)            
            return {"success": True, "message": "Local creado correctamente.", "id": data.get("id")}        
        except Exception as e:
            raise e
        
    def get_locals(self):
        try:            
            return {"success": True, "data": self.repository.get_locals()}
        except Exception as e:
            raise e
        
    def get_local_by_id(self, local_id: int):
        try:
            data = self.repository.get_local_by_id(local_id)
            if data:
                return {"success": True, "data": data}
            else:
                return {"success": False, "message": "El local no existe."}    
        except Exception as e:
            raise e
        
    def update_local(self, local_id: int, local: LocalUpdate):
        try:
            self.repository.update_local(local_id, local)
            return {"success": True, "message": "Local actualizado correctamente."}
        except Exception as e:
            raise e
        
    def delete_local(self, local_id: int):
        try:
            self.repository.delete_local(local_id)
            return {"success": True, "message": "Local eliminado correctamente."}
        except Exception as e:
            raise e