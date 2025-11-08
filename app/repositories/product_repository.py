from psycopg2.extensions import cursor
from ..schemas import Product, ProductCreate, ProductUpdate

class ProductRepository:
    """
    Realiza operaciones a los productos en la base de datos
    """
    def __init__(self, cursor: cursor):
        self.cursor = cursor

    def create_product(self, product: ProductCreate):
        """
        Crea un nuevo producto
        """
        query = "CALL prc_producto_insertar(%s, %s, %s, %s)"
        self.cursor.execute(query, (product.producto, product.categoria, product.marca, product.empresa))
    
    def get_products(self):
        """
        Retorna todos los productos
        """
        query = "SELECT * FROM func_productos_recuperar()"
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def get_product_by_id(self, product_id: int):
        """
        Retorna un producto identificado por el id
        """
        query = f"SELECT * FROM func_productos_recuperar() WHERE id = {product_id}"
        self.cursor.execute(query)
        return self.cursor.fetchone()
    
    def update_product(self, product_id: int, product: ProductUpdate):
        """
        Actualiza los datos de un producto
        """
        query = "CALL prc_producto_actualizar(%s, %s, %s, %s, %s)"
        self.cursor.execute(query, (product_id, product.producto, product.categoria, product.marca, product.empresa))

    def delete_product(self, product_id: int):
        """
        Elimina un producto
        """
        query = f"CALL prc_producto_eliminar({product_id})"
        self.cursor.execute(query)