from pydantic import BaseModel, Field
from typing import List, Dict, Optional
import re

class Employee(BaseModel):
    id:int
    name:str = Field(
        ...,
        min_length=2,
        max_length=32,
        description="Name of the employee",
        examples=["Asmit Yadav"]
        )
    age:int = Field(..., ge=18, lt=60)
    department: Optional[str] = "General"
    Salary: Optional[float] = Field(..., gt= 10_000) 
    Email: str = Field(...,)
    
emp1 = {
    "id": 1,
    "name": "Asmit Yadav",
    "age": 20,
    "department": "NebulaAI",
    "Salary" : 4_50_000,
    "Email": "asmityadav@dev.com",
}

emp1 = Employee(**emp1)
print(emp1)