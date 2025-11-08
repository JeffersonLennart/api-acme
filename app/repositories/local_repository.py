from psycopg2.extensions import cursor
from ..schemas import Local, LocalCreate, LocalUpdate

class LocalRepository:
    """
    Realiza operaciones a los locales en la base de datos
    """
    def __init__(self, cursor: cursor):
        self.cursor = cursor

    def create_local(self, local: LocalCreate):
        """
        Crea un nuevo local
        """
        query = "CALL prc_local_insertar(%s, %s, %s)"
        self.cursor.execute(query, (local.local, local.cliente, local.territorio))
    
    def get_locals(self):
        """
        Retorna todos los locales
        """
        query = "SELECT * FROM func_locales_recuperar()"
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def get_local_by_id(self, local_id: int):
        """
        Retorna un local identificado por el id
        """
        query = f"SELECT * FROM func_locales_recuperar() WHERE id = {local_id}"
        self.cursor.execute(query)
        return self.cursor.fetchone()
    
    def update_local(self, local_id: int, local: LocalUpdate):
        """
        Actualiza los datos de un local
        """
        query = "CALL prc_local_actualizar(%s, %s, %s, %s)"
        self.cursor.execute(query, (local_id, local.local, local.cliente, local.territorio))

    def delete_local(self, local_id: int):
        """
        Elimina un local
        """
        query = f"CALL prc_local_eliminar({local_id})"
        self.cursor.execute(query)