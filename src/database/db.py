from contextlib import asynccontextmanager

from fastapi import FastAPI
from core.settings import DB_USER,DB_HOST,DB_NAME,DB_PASSWORD
from sqlmodel import create_engine, Session, Field, SQLModel, select

DATABASE_URL = f"postgresql+psycopg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

#postgresql://aus1st:************@ep-dark-scene-148946-pooler.us-east-2.aws.neon.tech/employees?sslmode=require

engine = create_engine(DATABASE_URL, connect_args={"sslmode": "require"}, pool_recycle=300)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


    # When you create a context manager or an 
    # async context manager like above, what it does is that, 
    # before entering the with block, 
    #it will execute the code before the yield, and after exiting the with block, it will execute the code after the yield.

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Creating Database Tables...")
    create_db_and_tables()
    yield

def get_session():
    with Session(engine) as session:
        yield session



"""
Lifespan Events
You can define logic (code) that should be executed before the application starts up. This means that this code will be executed once, before the application starts receiving requests.

The same way, you can define logic (code) that should be executed when the application is shutting down. In this case, this code will be executed once, after having handled possibly many requests.

Because this code is executed before the application starts taking requests, and right after it finishes handling requests, it covers the whole application lifespan (the word "lifespan" will be important in a second 😉).

This can be very useful for setting up resources that you need to use for the whole app, and that are shared among requests, and/or that you need to clean up afterwards. For example, a database connection pool, or loading a shared machine learning model.
"""