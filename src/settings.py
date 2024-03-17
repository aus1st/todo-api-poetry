from starlette.config import Config
from starlette.datastructures import Secret

try:
    config = Config(".env")
except FileNotFoundError:
    config = Config()


DB_USER= config("DB_USER", cast=Secret)
DB_PASSWORD=config("DB_PASSWORD", cast=Secret)
DB_HOST=config("DB_HOST", cast=Secret)
#DB_PORT=3306
DB_NAME=config("DB_NAME", cast=Secret)

