from pydantic import BaseModel

class ProductBase(BaseModel):
    producto: str
    categoria: str
    marca: str
    empresa: str

class Product(BaseModel):
    id: int
    producto: str
    categoria: str
    marca: str
    empresa: str

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass