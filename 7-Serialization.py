from pydantic import BaseModel, ConfigDict 
from typing import List
from datetime import datetime

class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    createdAt: datetime
    address: Address
    tags: List[str] = []

    model_config = ConfigDict(
        json_encoders={datetime: lambda v: v.strftime('%d-%m-%Y %H:%M:%S')}
    )

# create a user instance
user = User(
    id= 1,
    name= "asmit yadav",
    email= "asmityadav@dev.com",
    createdAt = datetime(2024, 3, 15, 14, 30),
    address= Address(
        street = "Buttibori",
        city = "Nagpur",
        zip_code = "441108"
    ),
    is_active = False,
    tags = ["premium", "subscriber"],
)

# Using model_dump() -> dict
python_dict = user.model_dump()
print(python_dict)

print(f"="*120)

# Using model_dump_json()
json_str = user.model_dump_json()
print(json_str)