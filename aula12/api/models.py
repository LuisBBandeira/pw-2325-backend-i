from pydantic import BaseModel


class Product(BaseModel):
    name: str
    sku: int
    price: str
    enabled: bool
    id: str