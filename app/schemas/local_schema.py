from pydantic import BaseModel, ConfigDict

class LocalBase(BaseModel):
    local: str
    cliente: str
    territorio: str
    model_config = ConfigDict(extra="forbid")

class Local(BaseModel):
    id: int
    local: str
    cliente: str
    territorio: str
    model_config = ConfigDict(extra="forbid")

class LocalCreate(LocalBase):
    pass

class LocalUpdate(LocalBase):
    pass