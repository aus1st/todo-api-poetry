

from datetime import datetime
from sqlmodel import SQLModel,Field
from typing import Optional

from models.todo import TodoBase

class Todo(TodoBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    

class TodoCreate(TodoBase):    
    pass

class TodoRead(TodoBase):
    id: int

class TodoUpdate(TodoBase):
    pass