from psycopg2.extensions import cursor
from ..schemas import Client, ClientCreate, ClientUpdate


class ClientRepository():
    """
    Realiza operaciones a los clientes en la base de datos
    """

    def __init__(self, cursor: cursor):
        self.cursor = cursor

    def create_client(self, client: ClientCreate):
        """
        Crea un nuevo cliente
        """
        query = "SELECT func_cliente_insertar(%s, %s) AS id"
        self.cursor.execute(query, (client.cliente, client.industria))
        return self.cursor.fetchone()

    def get_clients(self):
        """
        Recupera todos los clientes
        """
        query = "SELECT * FROM func_clientes_recuperar()"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_client_by_id(self, client_id: int):
        """
        Recupera un cliente por su id
        """
        query = f"SELECT * FROM func_clientes_recuperar() WHERE id = {client_id}"
        self.cursor.execute(query)
        return self.cursor.fetchone()

    def update_client(self, client_id: int, client: ClientUpdate):
        """
        Actualiza los datos de un cliente
        """
        query = "CALL prc_cliente_actualizar(%s, %s, %s)"
        self.cursor.execute(
            query, (client_id, client.cliente, client.industria))

    def delete_client(self, cliente_id: int):
        """
        Elimina un cliente
        """
        query = f"CALL prc_cliente_eliminar({cliente_id})"
        self.cursor.execute(query)
