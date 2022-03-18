from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

# CORS is needed because origin is combination (protocol/domain/port)

app = FastAPI()

from db import (
    fetch_all_todos,
    fetch_one_todo,
    update_todo,
    create_todo,
    remove_todo
)
from model import Todo

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Ping": "Pong"}

@app.get("/api/todo")
async def get_todo():
    response = await fetch_all_todos()
    return response

@app.get("/api/todo/{title}", response_model=Todo)
async def get_todo_by_id(title):
    response = await fetch_one_todo(title)
    if response:
        return response
    raise HTTPException(404, f"no todo item with title: {title}")

@app.post("/api/todo", response_model=Todo)
async def post_todo(todo: Todo):
    print("hello")
    response = await create_todo(todo.dict())
    if response:
        return response
    raise HTTPException(400, "Something went wrong/bad request")

@app.put("/api/todo{titile}", response_model=Todo)
async def put_todo(title:str, desc):
    response = await update_todo(title, desc)
    if response:
        return response
    raise HTTPException(404, f"no todo item with title: {title}")

@app.delete("/api/todo{title}")
async def delete_todo(title):
    response = await remove_todo(title)
    if response:
        return "successfully deleted todo"
    raise HTTPException(404, "Something went wrong/bad request")

