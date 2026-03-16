```python
# Import necessary libraries
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields

# Initialize the database
db = SQLAlchemy()

# Define the Pony model
class Pony(db.Model):
    """Pony model"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    breed = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

# Define the Pony schema
class PonySchema(Schema):
    """Pony schema"""
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    breed = fields.Str(required=True)
    age = fields.Int(required=True)
```

###