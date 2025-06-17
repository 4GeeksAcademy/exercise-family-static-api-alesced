"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
# from models import Person


app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# Create the jackson family object
jackson_family = FamilyStructure("Jackson")


# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code


# Generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)


@app.route('/members', methods=['GET'])
def get_all_members():
    return jsonify(jackson_family.get_all_members()), 200

@app.route('/members/<int:member_id>', methods=['GET'])
def get_member(member_id):
    member = jackson_family.get_member(member_id)
    if member is None or member_id < 0:
        return jsonify({"msg": "Miembro no encontrado"}, 404)
    return jsonify(member), 200

@app.route('/members', methods=['POST'])
def add_member():
    member_data = request.get_json()
    new_member = jackson_family.add_member(member_data)
    return jsonify(new_member), 200 

@app.route('/members/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    removed_member = jackson_family.delete_member(member_id)
    if removed_member is None:
        return jsonify({"error": "Miembro no encontrado", "done": False}), 404
    return jsonify({"msg": "Miembro eliminado", "done": True, "member": removed_member}), 200

# This only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
