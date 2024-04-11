from typing import List
from fastapi import APIRouter
from faker import Faker
from api.models import Product

fake = Faker()

router= APIRouter(prefix="/product", tags=["Products"])


@router.get("")
def get_all_products()-> List[Product]:

    total_rows=20

    result = [
        Product(
            id=fake.isbn10(),
            name=" ".join(fake.words(nb=2)),
            price=fake.pricetag(),
            enabled=True,
            sku=100
        )
        for _ in range(total_rows)
    ]
    return result 