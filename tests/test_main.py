from fastapi.testclient import TestClient
from sqlmodel import Field, Session, SQLModel, create_engine, select
from database.db import get_session
from schemas.TodoSchema import Todo, TodoCreate
from main import app
from core import settings

TEST_DATABASE_URL = f"postgresql+psycopg://{settings.TEST_DB_USER}:{settings.TEST_DB_PASSWORD}@{settings.TEST_DB_HOST}/{settings.TEST_DB_NAME}"




def test_read_main():
    client = TestClient(app=app)
    response = client.get("/")
    assert response.status_code==200
    assert response.json() == {"Hello": "World"}

def test_add_todo():
    engine = create_engine(TEST_DATABASE_URL, connect_args={"sslmode": "require"}, pool_recycle=300)
    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:

        def get_session_override():
            return session
        
        app.dependency_overrides[get_session] = get_session_override
        client = TestClient(app=app)

        todo_content = TodoCreate(
        title = "test",
        description = "test",
        is_completed = False
        )
        response = client.post("/todos", json={"todo":todo_content})

        data = response.json()
        assert response.status_code == 200
        assert data["content"] == todo_content

def test_read_todos():
    engine = create_engine(TEST_DATABASE_URL, connect_args={"sslmode": "require"}, pool_recycle=300)
    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:

        def get_session_override():
            return session
        
        app.dependency_overrides[get_session] = get_session_override
        client = TestClient(app=app)

        response = client.get('/todos')
        assert response.status_code==200


