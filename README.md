# E-commerce-Product-Management-API

This is a RESTful API built with Flask for managing products in an e-commerce application.

##Setup Instructions
Requirements
Python 3.x
Flask
SQLAlchemy (for database interaction, optional if using in-memory data)
Installation
Clone this repository to your local machine:
bash
Copy code
git clone https://github.com/your-username/e-commerce-api.git
Navigate to the project directory:
bash
Copy code
cd e-commerce-api
Create a virtual environment (optional but recommended):
Copy code
python3 -m venv venv
Activate the virtual environment:
On Windows:
Copy code
venv\Scripts\activate
On macOS/Linux:
bash
Copy code
source venv/bin/activate
Install the required dependencies:
Copy code
pip install -r requirements.txt
Configuration
Configure database settings (if using a database):
Open config.py and modify the database URI based on your setup.
Alternatively, configure an in-memory database or use SQLite for testing purposes.
Running the API
Make sure your virtual environment is activated.
Run the Flask application:
arduino
Copy code
flask run
The API will be accessible at http://127.0.0.1:5000/.
