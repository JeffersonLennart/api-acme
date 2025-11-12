from fastapi import APIRouter, Depends, HTTPException, status
from psycopg2.errors import RaiseException
from ..schemas import Client, ClientCreate, ClientUpdate
from ..controllers import ClientController
from ..db import get_db


router = APIRouter(prefix="/clients", tags=["Clients"])


@router.post("/")
def create_client(client: ClientCreate, db_cursor=Depends(get_db)):
    try:
        # Se instancia el controlador, pasándole el cursor
        controller = ClientController(db_cursor)
        # Se crea el cliente
        result = controller.create_client(client)
        return result
    except RaiseException as e:
        # Error del cliente
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=e.diag.message_primary
        )
    except Exception as e:
        # Error del servidor
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )


@router.get("/", response_model=list[Client])
def get_clients(db_cursor=Depends(get_db)):
    try:
        # Se instancia el controlador, pasándole el cursor
        controller = ClientController(db_cursor)
        # Se recupera los clientes
        result = controller.get_clients()
        return result.get("data")
    except Exception as e:
        # Error del servidor
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )


@router.get("/{client_id}", response_model=Client)
def get_client_by_id(client_id: int, db_cursor=Depends(get_db)):
    try:
        # Se instancia el controlador, pasándole el cursor
        controller = ClientController(db_cursor)
        # Se valida el resultado
        result = controller.get_client_by_id(client_id)
        if result.get('success'):
            return result.get('data')
        else:
            # Error del cliente
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=result.get('message')
            )
    except HTTPException:
        raise
    except Exception as e:
        # Error del servidor
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )


@router.put("/{client_id}")
def update_client(client_id: int, client: ClientUpdate, db_cursor=Depends(get_db)):
    try:
        # Se instancia el controlador, pasándole el cursor
        controller = ClientController(db_cursor)
        # Se actualiza el local
        result = controller.update_client(client_id, client)
        return result
    except RaiseException as e:
        # Error del cliente
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=e.diag.message_primary
        )
    except Exception as e:
        # Error del servidor
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )


@router.delete("/{client_id}")
def delete_client(client_id: int, db_cursor=Depends(get_db)):
    try:
        # Se instancia el controlador, pasándole el cursor
        controller = ClientController(db_cursor)
        # Se elimina el local
        result = controller.delete_client(client_id)
        return result
    except RaiseException as e:
        # Error del cliente
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=e.diag.message_primary
        )
    except Exception as e:
        # Error del servidor
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
