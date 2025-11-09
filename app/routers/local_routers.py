from fastapi import APIRouter, Depends, HTTPException, status
from psycopg2.errors import RaiseException
from ..schemas import Local, LocalCreate, LocalUpdate
from ..controllers import LocalController
from ..db import get_db

router = APIRouter(prefix="/locals", tags=["Locals"])

@router.post("/")
def create_local(local: LocalCreate, db_cursor=Depends(get_db)):
    try:
        # Se instancia el controlador, pasándole el cursor
        controller = LocalController(db_cursor)
        # Se crea el local        
        result = controller.create_local(local)
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

@router.get("/", response_model=list[Local])
def get_locals(db_cursor=Depends(get_db)):
    try:
        # Se instancia el controlador, pasándole el cursor
        controller = LocalController(db_cursor)
        # Se recupera los locales
        result = controller.get_locals()
        return result.get("data")
    except Exception as e:
        # Error del servidor
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@router.get("/{local_id}", response_model=Local)
def get_local_by_id(local_id: int, db_cursor=Depends(get_db)):
    try:
        # Se instancia el controlador, pasándole el cursor
        controller = LocalController(db_cursor)
        # Se valida el resultado
        result = controller.get_local_by_id(local_id)        
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
    
@router.put("/{local_id}")
def update_local(local_id: int, local: LocalUpdate, db_cursor=Depends(get_db)):
    try:
        # Se instancia el controlador, pasándole el cursor
        controller = LocalController(db_cursor)
        # Se actualiza el local
        result = controller.update_local(local_id, local)
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

@router.delete("/{local_id}")
def delete_local(local_id: int, db_cursor=Depends(get_db)):
    try:
        # Se instancia el controlador, pasándole el cursor
        controller = LocalController(db_cursor)
        # Se elimina el local
        result = controller.delete_local(local_id)
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