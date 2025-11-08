from pydantic import BaseModel

class LocalBase(BaseModel):
    local: str
    cliente: str
    territorio: str

class Local(BaseModel):
    id: int
    local: str
    cliente: str
    territorio: str

class LocalCreate(LocalBase):
    pass

class LocalUpdate(LocalBase):
    pass