from pydantic import BaseModel
from typing import TypedDict

class Product(BaseModel):
    id: str
    name: str
    price: float
    inStock: bool
    
Products=[
    {
        "id": "IP13",
        "name": "iPhone 13",
        "price": 999.99,
        "inStock": True
    },
    {
        "id": "IP14",
        "name": "iPhone 14",
        "price": 1099.99,
        "inStock": True
    },
    {
        "id": "IP15",
        "name": "iPhone 15",
        "price": 1299.99,
        "inStock": False
    }
]

for product in Products:
    if product["inStock"] == True:
        product = Product(**product)
        print(product)