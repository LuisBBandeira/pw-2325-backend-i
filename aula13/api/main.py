from fastapi import FastAPI
from api.routes import (
    products
)


api = FastAPI(
    title="Product API",
    description="This API provides data for our catalog",
)

routers = [
    products.router
]

for router in routers:
    api.include_router(router=router)