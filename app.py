from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask import request



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
db = SQLAlchemy(app)

# Product Model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Product {self.title}>'

# Routes
@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'Welcome to the E-commerce API'})

@app.route('/products', methods=['GET'])
def get_all_products():
    products = Product.query.all()
    output = []
    for product in products:
        product_data = {'id': product.id, 'title': product.title, 'description': product.description, 'price': product.price}
        output.append(product_data)
    return jsonify({'products': output})

@app.route('/products/<int:id>', methods=['GET'])
def get_product_by_id(id):
    print(f'Received request for product ID: {id}') 
    product = Product.query.get_or_404(id)
    product_data = {'id': product.id, 'title': product.title, 'description': product.description, 'price': product.price}
    return jsonify(product_data)

@app.route('/create_product', methods=['GET', 'POST'])
def create_product_form():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        price = float(request.form['price'])
        
        new_product = Product(title=title, description=description, price=price)
        db.session.add(new_product)
        db.session.commit()
        
        return jsonify({'message': 'Product created successfully'}), 201

    # Render a form for users to input product details
    return '''
    <form method="POST">
        <label for="title">Title:</label><br>
        <input type="text" id="title" name="title"><br>
        <label for="description">Description:</label><br>
        <textarea id="description" name="description"></textarea><br>
        <label for="price">Price:</label><br>
        <input type="number" step="0.01" id="price" name="price"><br><br>
        <input type="submit" value="Create Product">
    </form>
    '''

@app.route('/update_products/<int:id>', methods=['GET', 'POST'])
def update_product_form(id):
    if request.method == 'POST':
        # Check if the form submission contains a hidden _method field with PUT value
        if request.form.get('_method') == 'PUT':
            product = Product.query.get_or_404(id)

            # Update product details based on form data
            product.title = request.form['title']
            product.description = request.form['description']
            product.price = float(request.form['price'])

            db.session.commit()
            return jsonify({'message': 'Product updated successfully'})

    # Render a form for users to input updated product details
    product = Product.query.get_or_404(id)
    return '''
    <form method="POST">
        <input type="hidden" name="_method" value="PUT"> <!-- Hidden field for method override -->
        <label for="title">Title:</label><br>
        <input type="text" id="title" name="title" value="{}"><br>
        <label for="description">Description:</label><br>
        <textarea id="description" name="description">{}</textarea><br>
        <label for="price">Price:</label><br>
        <input type="number" step="0.01" id="price" name="price" value="{}"><br><br>
        <input type="submit" value="Update Product">
    </form>
    '''.format(product.title, product.description, product.price)

from flask import request, jsonify

@app.route('/delete_product/<int:id>', methods=['GET', 'POST'])
def delete_product_form(id):
    if request.method == 'POST':
        # Check if the form submission contains a hidden _method field with DELETE value
        if request.form.get('_method') == 'DELETE':
            product = Product.query.get_or_404(id)

            # Delete the product from the database
            db.session.delete(product)
            db.session.commit()
            
            return jsonify({'message': 'Product deleted successfully'})

    # Render a form for users to confirm product deletion
    product = Product.query.get_or_404(id)
    return '''
    <form method="POST">
        <input type="hidden" name="_method" value="DELETE"> <!-- Hidden field for method override -->
        <p>Are you sure you want to delete the following product?</p>
        <p>Title: {title}</p>
        <p>Description: {description}</p>
        <p>Price: {price}</p>
        <input type="submit" value="Delete Product">
    </form>
    '''.format(title=product.title, description=product.description, price=product.price)







if __name__ == '__main__':
    app.run(debug=True)



