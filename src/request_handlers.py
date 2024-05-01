from src import app, Item


@app.route("/api/items")
def get_items():
    items = Item.query.all()
    return {
        "items": [
            {
                "id": i.id,
                "category_id": i.category_id,
                "name": i.name,
            }
            for i in items
        ]
    }
