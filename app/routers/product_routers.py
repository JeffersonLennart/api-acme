from fastapi import APIRouter, Depends, HTTPException, status
from psycopg2.errors import RaiseException
from ..schemas import Product, ProductCreate, ProductUpdate
from ..controllers import ProductController
from ..db import get_db

router = APIRouter(prefix="/products", tags=["Products"])

@router.post("/")
def create_product(product: ProductCreate, db_cursor=Depends(get_db)):
    try:
        # Se instancia el controlador, pasándole el cursor
        controller = ProductController(db_cursor)
        # Se crea el producto
        result = controller.create_product(product)
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

@router.get("/", response_model=list[Product])
def get_products(db_cursor=Depends(get_db)):
    try:
        # Se instancia el controlador, pasándole el cursor
        controller = ProductController(db_cursor)
        # Se recupera los productes
        result = controller.get_products()
        return result.get("data")
    except Exception as e:
        # Error del servidor
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@router.get("/{product_id}", response_model=Product)
def get_product_by_id(product_id: int, db_cursor=Depends(get_db)):
    try:
        # Se instancia el controlador, pasándole el cursor
        controller = ProductController(db_cursor)
        # Se valida el resultado
        result = controller.get_product_by_id(product_id)        
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
    
@router.put("/{product_id}")
def update_product(product_id: int, product: ProductUpdate, db_cursor=Depends(get_db)):
    try:
        # Se instancia el controlador, pasándole el cursor
        controller = ProductController(db_cursor)
        # Se actualiza el producto
        result = controller.update_product(product_id, product)
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

@router.delete("/{product_id}")
def delete_product(product_id: int, db_cursor=Depends(get_db)):
    try:
        # Se instancia el controlador, pasándole el cursor
        controller = ProductController(db_cursor)
        # Se elimina el producto
        result = controller.delete_product(product_id)
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