from fastapi import FastAPI, Depends
from pydantic import BaseModel, EmailStr

app = FastAPI()

class UserSignup(BaseModel):
    Username: str
    email: EmailStr
    password: str

class Settings(BaseModel):
    app_name: str = "Malin-1"
    admin_email: str = 'malin@galaxy.com'
    
def get_settings():
    return Settings()

@app.post('/signup')
def signup(user: UserSignup):
    return {'message': f'User {user.Username} Signed up successfully'}

@app.get('/settings')
def settings(settings: Settings = Depends(get_settings)):
    return settings.model_dump_json()

