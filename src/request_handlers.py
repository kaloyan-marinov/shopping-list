from flask import render_template, request

from src import Item, app


@app.route("/api/items")
def get_items():
    items = Item.query.all()
    for_backend = False if request.args.get("for_backend") == "false" else True
    return {
        "items": [i.to_dict(for_backend=for_backend) for i in items],
    }


@app.route("/")
def index():
    return render_template("ajax_table.html")
