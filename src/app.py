from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Category(db.Model):
    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True, nullable=False)

    items = db.relationship(
        "Item",
        lazy="dynamic",
        backref="category",
    )


class Item(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True, nullable=False)

    category_id = db.Column(
        db.Integer,
        db.ForeignKey("categories.id"),
        nullable=False,
    )


@app.route("/api/items")
def get_items():
    return {
        "items": [
            {
                "id": 1,
                "category": "vegetable",
                "name": "broccoli",
            },
            {
                "id": 2,
                "category": "household",
                "name": "hand soap",
            },
            {
                "id": 3,
                "category": "hygiene",
                "name": "toothpaste",
            },
        ]
    }
