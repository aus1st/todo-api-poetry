from fastapi import FastAPI
from core import settings

from typing import Annotated, List
from fastapi import  Depends, HTTPException
from sqlmodel import Session
from database.db import get_session
from schemas.TodoSchema import TodoCreate, TodoRead
from util.todo_crud import add_new_todo, get_all_todos

app = FastAPI(
    title= settings.TITLE,
    description= settings.DESCRIPTION,
    version=settings.API_VERSION,
    contact= settings.CONTACT,
    servers= settings.SERVERS
)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/todos", response_model=TodoRead)
async def create_todo(todo: TodoCreate,
                      db:Session = Annotated[Session,Depends(get_session)]
                      ):
    db_todo = add_new_todo(db,todo)
    if not db_todo:
        raise HTTPException(status_code=406, detail="Error creating Todo!")
    return db_todo


@app.get("/todos", response_model=List[TodoRead])
async def read_todos(db:Session = Annotated[Session,Depends(get_session)]):
    todos = get_all_todos(db)
    if not todos:
        raise HTTPException(status_code=406, detail="Error getting Todos!")
    return todos
