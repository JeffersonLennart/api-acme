from pydantic import BaseModel, ConfigDict


class Client(BaseModel):
    id: int
    cliente: str
    industria: str
    model_config = ConfigDict(extra='forbid')


class ClientBase(BaseModel):
    cliente: str
    industria: str
    model_config = ConfigDict(extra='forbid')


class ClientCreate(ClientBase):
    pass


class ClientUpdate(ClientBase):
    pass
