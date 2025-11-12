from ..repositories import ClientRepository
from ..schemas import Client, ClientCreate, ClientUpdate


class ClientController():
    """
    Clase que contiene la lógica para manejar las peticiones para clientes.    
    """

    def __init__(self, db_cursor):
        # El cursor se usa para instanciar el Repository.
        self.repository = ClientRepository(db_cursor)

    def create_client(self, client: ClientCreate):
        try:
            data = self.repository.create_client(client)
            return {"success": True, "message": "Cliente creado correctamente.", "id": data.get("id")}
        except Exception as e:
            raise e

    def get_clients(self):
        try:
            return {"success": True, "data": self.repository.get_clients()}
        except Exception as e:
            raise e

    def get_client_by_id(self, client_id: int):
        try:
            data = self.repository.get_client_by_id(client_id)
            if data:
                return {"success": True, "data": data}
            else:
                return {"success": False, "message": "El cliente no existe."}
        except Exception as e:
            raise e

    def update_client(self, client_id: int, client: ClientUpdate):
        try:
            self.repository.update_client(client_id, client)
            return {"success": True, "message": "Cliente actualizado correctamente."}
        except Exception as e:
            raise e

    def delete_client(self, client_id: int):
        try:
            self.repository.delete_client(client_id)
            return {"success": True, "message": "Cliente eliminado correctamente."}
        except Exception as e:
            raise e
