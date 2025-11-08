from fastapi import FastAPI
from .routers import local_routers, product_routers

app = FastAPI(title="API-ACME")

app.include_router(local_routers.router)
app.include_router(product_routers.router)