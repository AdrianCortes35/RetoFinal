import pytest
from app import create_app, db
from app.models import Data


@pytest.fixture
def app():
    app = create_app("development")
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()


def test_insert_data(client):
    response = client.post(
        "/data",
        json={"name": "Test User"}
    )
    assert response.status_code == 200
    assert b"Data inserted successfully" in response.data


def test_get_all_data(client):
    # Insert sample data
    client.post(
        "/data",
        json={"name": "Test User"}
    )

    response = client.get("/data")
    assert response.status_code == 200
    assert b"Test User" in response.data


def test_delete_data(client):
    # Insert sample data
    client.post(
        "/data",
        json={"name": "Test User"}
    )

    # Get the id of the inserted data
    data_id = Data.query.filter_by(name="Test User").first().id

    response = client.delete(f"/data/{data_id}")
    assert response.status_code == 200
    assert b"Data deleted successfully" in response.data

def test_insert_existing_data(client):
    # Insert sample data
    client.post(
        "/data",
        json={"name": "Test User"}
    )

    # Try to insert data with the same name again
    response = client.post(
        "/data",
        json={"name": "Test User"}
    )
    assert response.status_code == 409
    assert b"Data already exists" in response.data

def test_delete_nonexistent_data(client):
    # Try to delete data that doesn't exist
    response = client.delete("/data/999")
    assert response.status_code == 404
    assert b"Data not found" in response.data        