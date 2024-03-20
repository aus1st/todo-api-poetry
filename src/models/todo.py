

from datetime import datetime
from sqlmodel import SQLModel,Field
from typing import Optional
#id	title	description	is_completed	created_at	created_by	updated_at
class TodoBase(SQLModel):
    title: str = Field(index=True)
    description: str = Field(default=None)
    is_completed: bool = Field(default=False)
    created_at: datetime =Field(default_factory=datetime.now)
    created_by: Optional[int] = Field(default=1)
    updated_at: Optional[datetime] =Field(default=None)    
    updated_by: Optional[int] 


    