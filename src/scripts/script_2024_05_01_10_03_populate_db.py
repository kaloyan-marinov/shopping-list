from src import Category, Item, app, db

if __name__ == "__main__":
    with app.app_context():
        c_1 = Category(name="vegetable")
        c_2 = Category(name="household")
        c_3 = Category(name="hygiene")
        db.session.add(c_1)
        db.session.add(c_2)
        db.session.add(c_3)
        db.session.commit()

        i_1 = Item(name="broccoli", category_id=c_1.id)
        i_2 = Item(name="hand soap", category_id=c_2.id)
        i_3 = Item(name="toothpaste", category_id=c_3.id)
        db.session.add(i_1)
        db.session.add(i_2)
        db.session.add(i_3)
        db.session.commit()
