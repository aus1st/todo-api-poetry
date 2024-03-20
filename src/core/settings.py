from starlette.config import Config
from starlette.datastructures import Secret

try:
    config = Config(".env")
except FileNotFoundError:
    config = Config()


API_VERSION: str = "1.0.0"
TITLE: str = "Todo by FastApi with POETRY"
DESCRIPTION: str = "CRUD operations using FastApi"
CONTACT: dict = {
        "name": "Ahmed uddin Siddiqui",
        "url": "https://www.github.com/aus1st",
        "email": "aus1st@gmail.com",
    }
SERVERS: list = [
    {
        "url": "http://0.0.0.0:8000", 
        "description": "Development Server"
    }
    
]
DB_USER= config("DB_USER", cast=Secret)
DB_PASSWORD=config("DB_PASSWORD", cast=Secret)
DB_HOST=config("DB_HOST", cast=Secret)
#DB_PORT=3306
DB_NAME=config("DB_NAME", cast=Secret)

TEST_DB_USER= config("TEST_DB_USER", cast=Secret)
TEST_DB_PASSWORD=config("TEST_DB_PASSWORD", cast=Secret)
TEST_DB_HOST=config("TEST_DB_HOST", cast=Secret)
#TEST_DB_PORT=3306
TEST_DB_NAME=config("TEST_DB_NAME", cast=Secret)

