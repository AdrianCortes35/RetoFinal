from app import db


# Define a SQLAlchemy model
class Data(db.Model):
    # Define columns for the model
    id = db.Column(db.Integer, primary_key=True)  # Primary key column
    name = db.Column(db.String(100))              # Column for storing a string with a maximum length of 100 characters

    def __repr__(self):
        return f"<Data id={self.id} name={self.name}>"
