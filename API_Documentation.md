## E-commerce Product Management API Documentation
This API provides functionality for managing products in an e-commerce application.

### Base URL
The base URL for all endpoints is http://localhost:5000/ when running locally.

## Endpoints
### GET /

Description: Welcome message indicating the API is running.

Method: GET

#### Response:

{"message": "Welcome to the E-commerce API"}

### GET /products
Description: Retrieve all products.

Method: GET

#### Response:

{
  "products": [
    {"id": 1, "title": "Product 1", "description": "Description for Product 1", "price": 10.0},
    {"id": 2, "title": "Product 2", "description": "Description for Product 2", "price": 20.0}
  ]
}

### GET /products/<int:id>

Description: Retrieve a specific product by ID.

Method: GET

URL Parameter: id (integer) - The ID of the product to retrieve.

#### Response:

{"id": 1, "title": "Product 1", "description": "Description for Product 1", "price": 10.0}

### POST /create_product

Description: Create a new product.

Method: POST

Request Body:

{
  "title": "New Product",
  "description": "Description for New Product",
  "price": 15.0
}

#### Response:

{"message": "Product created successfully"}

### POST /update_products/<int:id>

Description: Update an existing product by ID.

Method: POST

URL Parameter: id (integer) - The ID of the product to update.

Request Body:

{
  "title": "Updated Product",
  "description": "Updated description",
  "price": 25.0
}

#### Response:

{"message": "Product updated successfully"}

### POST /delete_product/<int:id>

Description: Delete a product by ID.

Method: POST

URL Parameter: id (integer) - The ID of the product to delete.

#### Response:

{"message": "Product deleted successfully"}


### Note
For updating and deleting products, the respective endpoints /update_products/<int:id> and /delete_product/<int:id> accept POST requests with a hidden _method field in the form to simulate PUT and DELETE requests, respectively. This is done for compatibility with HTML forms.

