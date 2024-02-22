from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import config_dict

# Initialize SQLAlchemy object
db = SQLAlchemy()

# Function to create Flask application
def create_app(config_name):
    app = Flask(__name__)                                # Create Flask app instance
    app.config.from_object(config_dict[config_name])     # Load configuration from config dictionary based on config_name  
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////home/adrian123/RetoFinal/instance/db.db"     # Set the URI for the SQLite database

    # Initialize the database
    db.init_app(app)
    # Import blueprints/routes
    from app.routes import data_routes

    # Register blueprints
    app.register_blueprint(data_routes)

    return app
