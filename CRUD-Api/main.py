from fastapi import FastAPI
from pydantic import BaseModel

todos=[]
app=FastAPI()

class Todo(BaseModel):
    id:int
    title:str
    completed:bool
    
# CREATE  TODO USING POST METHOD     
@app.post("/todos")
def create_todo(todo:Todo):
    todos.append(todo)
    return {
        "msg":"Todo added",
        "data":todo
    }
#for all  todo 
@app.get("/todos")
def get_todos():
    return todos

# GET  TODO USING GET METHOD 
@app.get("/todos/{todo_id}")
def get_todo(todo_id:int):
    for todo in todos:
        if todo.id==todo_id:
            return todo
    return {"error": "id not found"}

# UPDATE TODO USING PUT METHOD 

@app.put("/todos/{todo_id}")
def update_todo(todo_id:int,updated_todo:Todo):
    for index,todo in enumerate(todos):
        if todo.id==todo_id:
            todos[index]=updated_todo
            return{
                "msg":"todo updated",
                "data":updated_todo
            }
    
    return {"error": "id not found"}
# DELETE TODO USING DELETE METHOD 
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id:int):
    for index,todo in enumerate(todos):
        if todo.id==todo_id:
            todos.pop(index)
            return {
                "msg":"Data deleted"
            } 
    return {"error": "id not found"}
    
                    
