from typing import List
from fastapi import APIRouter
from faker import Faker
from api.clients import get_products
from api.models import Product

fake = Faker()

router= APIRouter(prefix="/product", tags=["Products"])


@router.get("")
def get_all_products()-> List[Product]:
    result = [
        Product(**product)
        for product in get_products(db="/app/db.json")
    ]
    return result 