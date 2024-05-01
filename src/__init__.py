import os
import sys

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

DB_ENGINE_HOST = os.environ.get("DB_ENGINE_HOST")
DB_ENGINE_PORT = os.environ.get("DB_ENGINE_PORT")
POSTGRES_DB = os.environ.get("POSTGRES_DB")
POSTGRES_USER = os.environ.get("POSTGRES_USER")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")

if (
    DB_ENGINE_HOST is None
    or DB_ENGINE_PORT is None
    or POSTGRES_DB is None
    or POSTGRES_USER is None
    or POSTGRES_PASSWORD is None
):
    print("configuration for connecting to a database is missing - aborting...")
    sys.exit(1)


app = Flask(
    __name__,
    static_folder="static",
    template_folder="templates",
)
app.config["SECRET_KEY"] = os.environ["SECRET_KEY"]
app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@"
    f"{DB_ENGINE_HOST}:{DB_ENGINE_PORT}"
    f"/{POSTGRES_DB}"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db, directory="src/migrations")


from src.models import Category, Item  # noqa, isort: skip
from src import request_handlers  # noqa, isort: skip
