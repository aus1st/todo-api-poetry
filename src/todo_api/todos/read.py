from typing import Annotated,List
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from database.db import get_session
from schemas.TodoSchema import  TodoRead
from util.todo_crud import get_all_todos

router  = APIRouter()

@router.get("/todos", response_model=List[TodoRead])
async def read_todos(db:Session = Annotated[Session,Depends(get_session)]):
    todos = get_all_todos(db)
    if not todos:
        raise HTTPException(status_code=406, detail="Error getting Todos!")
    return todos