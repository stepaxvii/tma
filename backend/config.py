from os import getenv

from dotenv import load_dotenv

load_dotenv()

USER = getenv("DB_USER")
PASSWORD = getenv("DB_PASSWORD")
HOST = getenv("DB_HOST")
PORT = getenv("DB_PORT")
NAME = getenv("DB_NAME")

TORTOISE_ORM = {
    "connections": {
        "default": f"postgres://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}"
    },
    "apps": {
        "models": {
            "models": ["models", "aerich.models"],
            "default_connection": "default",
        }
    },
}
