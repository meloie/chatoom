from starlette.config import Config
from starlette.datastructures import URL

config = Config(".env")

DEBUG = config("DEBUG", cast=bool, default=False)
REDIS_URL = config("REDIS_URL", cast=str)
