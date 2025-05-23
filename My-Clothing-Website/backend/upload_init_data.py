from main import app
from application.models import db, Role, User ,Inventory,Product,Category
from werkzeug.security import generate_password_hash

with app.app_context():
    db.create_all()

    # Create roles
    if not Role.query.filter_by(name="admin").first():
        admin_role = Role(name="admin", description="Administrator role")
        db.session.add(admin_role)

    if not Role.query.filter_by(name="user").first():
        user_role = Role(name="user", description="User role")
        db.session.add(user_role)

    db.session.commit()

    # Create admin user
    if not User.query.filter_by(email="admin@gmail.com").first():
        admin_user = User(
            name="Admin User",
            email="admin@gmail.com",
            password=generate_password_hash("admin"),
            active=True
        )
        admin_user.roles.append(admin_role)
        db.session.add(admin_user)

    # Create initial categories
    if not Category.query.first():
        categories = [
            Category(name="Electronics"),
            Category(name="Books"),
            Category(name="Clothing"),
            Category(name="Home & Kitchen"),
        ]
        db.session.add_all(categories)
        db.session.commit()
        print("Categories created successfully.")

    # Create initial products
    if not Product.query.first():
        products = [
            Product(
                name="Smartphone",
                description="Latest model smartphone with advanced features.",
                category_id=1,
                price=699.99,
                discount=50.0,
                sku="ELEC123",
                image="smartphone.jpg",
            ),
            Product(
                name="Novel",
                description="A gripping mystery novel.",
                category_id=2,
                price=19.99,
                sku="BOOK123",
                image="novel.jpg",
            ),
            Product(
                name="T-Shirt",
                description="Comfortable cotton t-shirt.",
                category_id=3,
                price=15.99,
                discount=5.0,
                sku="CLOT123",
                image="tshirt.jpg",
            ),
            Product(
                name="Blender",
                description="Powerful blender for your kitchen needs.",
                category_id=4,
                price=49.99,
                sku="HOME123",
                image="blender.jpg",
            ),
        ]
        db.session.add_all(products)
        db.session.commit()
        print("Products created successfully.")

    # Add initial stock for inventory
    if not Inventory.query.first():
        inventory = [
            Inventory(product_id=1, stock=50, location="Warehouse A"),
            Inventory(product_id=2, stock=30, location="Warehouse B"),
            Inventory(product_id=3, stock=100, location="Warehouse C"),
            Inventory(product_id=4, stock=25, location="Warehouse D"),
        ]
        db.session.add_all(inventory)
        db.session.commit()
        print("Inventory created successfully.")

    # Commit all changes
    db.session.commit()
    print("Database initialized successfully!")
