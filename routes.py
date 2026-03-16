```python
# Import necessary libraries
from flask import Blueprint, request, jsonify
from models import db, Pony
from schemas import pony_schema, ponies_schema

# Initialize the blueprint
pony_blueprint = Blueprint('pony_blueprint', __name__)

# Define the routes
@pony_blueprint.route('/ponies', methods=['GET'])
def get_ponies():
    """Get all ponies"""
    try:
        ponies = Pony.query.all()
        return jsonify(ponies_schema.dump(ponies))
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@pony_blueprint.route('/ponies', methods=['POST'])
def create_pony():
    """Create a new pony"""
    try:
        data = request.get_json()
        errors = pony_schema.validate(data)
        if errors:
            return jsonify({'error': errors}), 400
        new_pony = Pony(data['name'], data['breed'], data['age'])
        db.session.add(new_pony)
        db.session.commit()
        return jsonify(pony_schema.dump(new_pony)), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@pony_blueprint.route('/ponies/<id>', methods=['GET'])
def get_pony(id):
    """Get a pony by id"""
    try:
        pony = Pony.query.get(id)
        if pony is None:
            return jsonify({'error': 'Pony not found'}), 404
        return jsonify(pony_schema.dump(pony))
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@pony_blueprint.route('/ponies/<id>', methods=['PUT'])
def update_pony(id):
    """Update a pony"""
    try:
        pony = Pony.query.get(id)
        if pony is None:
            return jsonify({'error': 'Pony not found'}), 404
        data = request.get_json()
        errors = pony_schema.validate(data)
        if errors:
            return jsonify({'error': errors}), 400
        pony.name = data['name']
        pony.breed = data['breed']
        pony.age = data['age']
        db.session.commit()
        return jsonify(pony_schema.dump(pony))
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@pony_blueprint.route('/ponies/<id>', methods=['DELETE'])
def delete_pony(id):
    """Delete a pony"""
    try:
        pony = Pony.query.get(id)
        if pony is None:
            return jsonify({'error': 'Pony not found'}), 404
        db.session.delete(pony)
        db.session.commit()
        return jsonify({'message': 'Pony deleted'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
```

###