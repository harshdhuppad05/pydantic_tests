from fastapi import FastAPI, Depends
from pydantic import BaseModel, EmailStr

app  =FastAPI()

class User(BaseModel):
    name : str
    email : EmailStr
    password : str


class Settings(BaseModel):
    name: str = "Admin"
    email: EmailStr = "john.blair@example-pet-store.com"

def get_settings(settings: Settings):
    return settings()


@app.post("/signup")
def signup(user: User):
    return {"message": f"Welcome {user.name}! Your email is {user.email}"}

@app.get("/settings")
def get_settings(settings: Settings = Depends(get_settings)):
    return settings