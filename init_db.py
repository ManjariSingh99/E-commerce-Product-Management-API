from app import app, db

# Create an application context
app.app_context().push()

# Drop existing tables (if any)
db.drop_all()

# Create the database tables
db.create_all()

# Add sample data
from app import Product  # Import Product model here
sample_product1 = Product(title='Laptop', description='High-performance laptop', price=999.99)
sample_product2 = Product(title='Mouse', description='Wireless mouse', price=19.99)

db.session.add(sample_product1)
db.session.add(sample_product2)

db.session.commit()

print('Database initialized successfully.')
