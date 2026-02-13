from market import app, db
from market.models import Item


def seed():
    with app.app_context():
        if Item.query.first():
            print("Items already present — skipping seeding.")
            return

        sample_items = [
            {
                'name': 'Mechanical Keyboard',
                'price': 120,
                'barcode': '123456789012',
                'description': 'A tactile mechanical keyboard with RGB lighting.'
            },
            {
                'name': 'Wireless Mouse',
                'price': 45,
                'barcode': '234567890123',
                'description': 'Ergonomic wireless mouse with long battery life.'
            },
            {
                'name': 'USB-C Hub',
                'price': 35,
                'barcode': '345678901234',
                'description': 'Compact USB-C hub with HDMI and Ethernet.'
            },
        ]

        for it in sample_items:
            item = Item(name=it['name'], price=it['price'], barcode=it['barcode'], description=it['description'])
            db.session.add(item)
        db.session.commit()
        print(f"Seeded {len(sample_items)} items into the database.")


if __name__ == '__main__':
    seed()
