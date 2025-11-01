from pydantic import BaseModel, field_validator, model_validator, computed_field

class User(BaseModel):
    Username: str
    age: int
    
    @field_validator('Username')
    def correct_username(cls, v):
        if(len(v)<6):
            raise ValueError("Username must be of atleast 6 characters")
        return v
    
    @field_validator('age')
    def validate_age(cls, v):
        if(v<18):
            raise ValueError("User must be an adult (18 years old and above)")
        return v

p1 = User(Username="Asmit Yadav", age=20)
# print(p1)



class Password(BaseModel):
    password: str
    confirm_password: str

    @model_validator(mode='after')
    def check_passwords_match(self):
        if self.password != self.confirm_password:
            raise ValueError('Passwords do not match')
        return self

pass1 = Password(password="Asmit@123", confirm_password="Asmit@123")
# print(pass1)


class FullName(BaseModel):
    first_name: str
    last_name: str

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

user = FullName(first_name="Asmit", last_name="Yadav")
# print(user.full_name)  

class User2(BaseModel):
    first_name: str
    last_name: str
    price: int
    Quantity: int

    @computed_field  
    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
    @computed_field
    @property
    def total_price(self) -> int:
        return self.price * self.Quantity


user = User2(first_name="Asmit", last_name="Yadav", price=100, Quantity=2)
print(user.full_name)             
print(user.total_price)     