from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()
class Address(BaseModel):
    PinCode:int
    country:str

class User(BaseModel):
    name:str
    age:int
    address:Address

@app.post("/user_created")
def user_created(user:User):
    return{
        "msg":"User created",
        "data":user
    }

