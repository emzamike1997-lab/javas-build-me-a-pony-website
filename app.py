```python
# Import necessary libraries
from flask import Flask
from routes import pony_blueprint
from models import db

# Initialize the app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pony.db'
db.init_app(app)

# Register the blueprint
app.register_blueprint(pony_blueprint)

# Create the database
with app.app_context():
    db.create_all()

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```

### Running the Application
To run the application, navigate to the project directory and execute the following commands:
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```
The application will start on port 5000. You can use a tool like curl or Postman to test the API endpoints.

### Example Use Cases
* Get all ponies: `curl http://localhost:5000/ponies`
* Create a new pony: `curl -X POST -H "Content-Type: application/json" -d '{"name": "Pony1", "breed": "Breed1", "age": 5}' http://localhost:5000/ponies`
* Get a pony by id: `curl http://localhost:5000/ponies/1`
* Update a pony: `curl -X PUT -H "Content-Type: application/json" -d '{"name": "Pony1", "breed": "Breed1", "age": 6}' http://localhost:5000/ponies/1`
* Delete a pony: `curl -X DELETE http://localhost:5000/ponies/1`