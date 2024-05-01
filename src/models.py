from src import db


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
    name = db.Column(db.String(128), unique=True, nullable=False)

    category_id = db.Column(
        db.Integer,
        db.ForeignKey("categories.id"),
        nullable=False,
    )

    def to_dict(self, for_backend: bool = True):
        d = {
            "id": self.id,
            "name": self.name,
        }
        if for_backend:
            d["category_id"] = self.category_id
        else:
            d["category"] = self.category.name
        return d
