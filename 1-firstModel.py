from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    IsActive: bool
    
input_data = {
    "id": 1,
    "name": "John Doe",
    "IsActive": True
}

user = User(**input_data)

print(user)