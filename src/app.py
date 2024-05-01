from flask import Flask


app = Flask(__name__)


@app.route("/api/items")
def get_items():
    return {
        "items": [
            {
                "id": 1,
                "category": "vegetable",
                "title": "broccoli",
            },
            {
                "id": 2,
                "category": "household",
                "title": "hand soap",
            },
            {
                "id": 3,
                "category": "hygiene",
                "title": "toothpaste",
            },
        ]
    }
