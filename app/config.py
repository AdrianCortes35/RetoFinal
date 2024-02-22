import os


class Config:
    # Secret key for the Flask app
    SECRET_KEY = os.environ.get("SECRET_KEY", "your_secret_key")

    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


# Dictionary to map environment names to configuration classes
config_dict = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
}
