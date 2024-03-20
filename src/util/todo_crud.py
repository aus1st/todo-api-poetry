


from sqlmodel import Session,select
from schemas.TodoSchema import Todo, TodoCreate


def add_new_todo(db:Session, todo: TodoCreate):
    try:
        db_todo = TodoCreate(
            title=todo.title,
            description=todo.description,
            is_completed=False,
            created_by=1, # to get this id from session
            updated_by=None,
            updated_at=None
        )
        db.add(db_todo)
        db.commit()
        db.refresh()
        return db_todo
    except Exception as e:
        raise e


def get_all_todos(db:Session):
    try:
       todos = db.exec(select(Todo)).all()
       return todos
    except Exception as e:
        raise e