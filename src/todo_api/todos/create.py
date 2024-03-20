from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from database.db import get_session
from schemas.TodoSchema import TodoCreate, TodoRead
from util.todo_crud import add_new_todo

router  = APIRouter()

@router.post("/todos", response_model=TodoRead)
async def create_todo(todo: TodoCreate,
                      db:Session = Annotated[Session,Depends(get_session)]
                      ):
    db_todo = add_new_todo(db,todo)
    if not db_todo:
        raise HTTPException(status_code=406, detail="Error creating Todo!")
    return db_todo