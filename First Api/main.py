from fastapi import FastAPI

app=FastAPI()
#home route
@app.get("/")
def home():
    return {"message":"welcome tp Fastapi home page"}

#about route
@app.get("/about")
def about():
    return {"message":"welcome tp Fastapi about page"}

#users
@app.get("/users")
def users():
    return {
        "users":["mohit","rohit","ammit"]
    }

