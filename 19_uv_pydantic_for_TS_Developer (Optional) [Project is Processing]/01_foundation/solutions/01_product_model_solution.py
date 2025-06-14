from pydantic import BaseModel

# TODO: Create Product mode with id, name , price, is_in_stock


class Product(BaseModel):
    id: int
    name: str
    price: float
    is_in_stock: bool = True  # default value


product_data = {
    "id": 100,
    "name": "Value Top T22IF Monitor",
    "price": 10000.00,
    "is_in_stock": True,
}

monitor = Product(**product_data)

print(monitor)
