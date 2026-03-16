```python
# Import necessary libraries
from marshmallow import Schema, fields
from models import PonySchema

# Define the Pony schema
pony_schema = PonySchema()
ponies_schema = PonySchema(many=True)
```

###