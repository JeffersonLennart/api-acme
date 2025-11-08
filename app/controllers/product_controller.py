from ..repositories import ProductRepository
from ..schemas import Product, ProductCreate, ProductUpdate
from psycopg2.errors import RaiseException

class ProductController:
    """
    Clase que contiene la lógica para manejar las peticiones para Productos.    
    """
    def __init__(self, db_cursor):
        # El cursor se usa para instanciar el Repository.
        self.repository = ProductRepository(db_cursor)

    def create_product(self, product: ProductCreate):
        try:
            self.repository.create_product(product)
            return {"success": True, "message": "Producto creado correctamente."}
        except Exception as e:
            raise e
        
    def get_products(self):
        try:            
            return {"success": True, "data": self.repository.get_products()}
        except Exception as e:
            raise e
        
    def get_product_by_id(self, product_id: int):
        try:
            data = self.repository.get_product_by_id(product_id)
            if data:
                return {"success": True, "data": data}
            else:
                return {"success": False, "message": "El producto no existe."}    
        except Exception as e:
            raise e
        
    def update_product(self, product_id: int, product: ProductUpdate):
        try:
            self.repository.update_product(product_id, product)
            return {"success": True, "message": "Producto actualizado correctamente."}
        except Exception as e:
            raise e
        
    def delete_product(self, product_id: int):
        try:
            self.repository.delete_product(product_id)
            return {"success": True, "message": "Producto eliminado correctamente."}
        except Exception as e:
            raise e