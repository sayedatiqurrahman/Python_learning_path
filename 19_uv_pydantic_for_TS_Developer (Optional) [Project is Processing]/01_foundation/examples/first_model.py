from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    is_active: bool


def example(id, name, is_active):
    print(f"id: {id}, name: {name}, is_active: {is_active}")


input_data = {"id": 100, "name": "Atiqur Rahman", "is_active": True}

# this ** is like spread operator in js / ts
user = User(**input_data)

example(**input_data)
print(user)
print({**input_data})
