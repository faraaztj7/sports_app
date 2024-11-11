import pytest
from app import create_app  # Import your app creation function
from app.models import Area  # Import your Area model


@pytest.fixture
def app():
    app = create_app()  # Assuming your app has a function to create the app
    with app.app_context():  # Ensure the app context is available for tests
        yield app


@pytest.fixture
def client(app):
    return app.test_client()  # Create a test client for making requests


def test_get_areas(client):
    """Test for getting all areas"""
    response = client.get('/areas/')  # Replace with your actual endpoint
    assert response.status_code == 200
    # You can add further assertions to check the response content


def test_get_area_by_id(client):
    """Test for getting an area by ID"""
    response = client.get('/areas/1')  # Replace with your actual endpoint and test ID
    assert response.status_code == 200
    # Further assertions can check the area data returned


def test_get_area_by_non_existing_id(client):
    """Test for getting an area by non-existing ID"""
    response = client.get('/areas/999')  # Replace with a non-existent ID
    assert response.status_code == 404  # Adjust the expected status code based on your error handling
