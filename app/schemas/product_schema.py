from pydantic import BaseModel, ConfigDict

class ProductBase(BaseModel):
    producto: str
    categoria: str
    marca: str
    empresa: str
    model_config = ConfigDict(extra="forbid")

class Product(BaseModel):
    id: int
    producto: str
    categoria: str
    marca: str
    empresa: str
    model_config = ConfigDict(extra="forbid")

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass