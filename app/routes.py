from flask import Blueprint, request, jsonify
from app.models import Data
from app import db

data_routes = Blueprint("data_routes", __name__)

# Route for inserting new data
@data_routes.route("/data", methods=["POST"])
def insert_data():
    data = request.json  # Assuming JSON data is sent for insertion
    new_data = Data(name=data.get("name")) # Create a new Data object

    # Check if data with the same name already exists   
    current_data = Data.query.filter_by(name=data.get("name")).first()
    if current_data:
        return {"message": "Data already exists"}, 409

    # Add the new data to the database session and commit changes
    db.session.add(new_data)
    db.session.commit()
    return jsonify({"message": "Data inserted successfully"})


# Route for retrieving all data
@data_routes.route("/data", methods=["GET"])
def get_all_data():
    data_list = [{"id": data.id, "name": data.name} for data in Data.query.all()]      # Retrieve all data from the database and format it as a list of dictionaries
    return jsonify(data_list)


# Route for deleting data by ID
@data_routes.route("/data/<int:id>", methods=["DELETE"])
def delete_data(id):
    element_to_delete = db.session.get(Data, id)    # Retrieve the data to delete by its ID
    if not element_to_delete:
        return {"message": "Data not found"}, 404

    # Delete the data from the database session and commit changes
    db.session.delete(element_to_delete)
    db.session.commit()
    return {"message": "Data deleted successfully"}
