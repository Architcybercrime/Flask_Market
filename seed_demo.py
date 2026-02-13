from market import db, app
from market.models import User, Item

with app.app_context():
    db.create_all()

    if not User.query.filter_by(username='demo').first():
        demo = User(username='demo', email_address='demo@example.com')
        demo.password = 'password123'
        db.session.add(demo)

    # sample items
    sample_items = [
        {'name': 'Laptop', 'price': 800, 'barcode': '111111111111', 'description': 'A fast laptop.'},
        {'name': 'Headphones', 'price': 120, 'barcode': '222222222222', 'description': 'Noise cancelling.'},
        {'name': 'Keyboard', 'price': 60, 'barcode': '333333333333', 'description': 'Mechanical keyboard.'},
        {'name': 'Mouse', 'price': 40, 'barcode': '444444444444', 'description': 'Wireless mouse.'},
    ]

    for it in sample_items:
        if not Item.query.filter_by(name=it['name']).first():
            item = Item(name=it['name'], price=it['price'], barcode=it['barcode'], description=it['description'])
            db.session.add(item)

    db.session.commit()
    print('Seed complete: demo user (password: password123) and sample items added.')
