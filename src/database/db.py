from settings import DB_USER,DB_HOST,DB_NAME,DB_PASSWORD
from sqlmodel import create_engine, Session, Field, SQLModel, select

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"


engine = create_engine(DATABASE_URL, connect_args={"sslmode": "require"}, pool_recycle=300)

SessionLocal = sess
