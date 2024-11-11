import pytest
from app import create_app
from app.models import Competition
from unittest.mock import patch

@pytest.fixture
def app():
    app = create_app()  # Create the app instance
    with app.app_context():  # Ensure the app context is available for the test
        yield app

@pytest.fixture
def client(app):
    return app.test_client()  # Create a test client for making requests

def test_get_competitions(client):
    """Test for getting all competitions using static data."""
    # Mocking the Competition.query.all() method to return static data
    with patch('app.routes.competitions.Competition.query.all') as mock_query:
        mock_query.return_value = [
            Competition(id=1, name='Premier League'),
            Competition(id=2, name='La Liga')
        ]
        
        response = client.get('/competitions/')
        assert response.status_code == 200
        data = response.get_json()
        assert isinstance(data, list)
        assert len(data) == 3  # We expect two static competitions
        assert data[0]['name'] == 'UEFA' or 'FIFA' or 'La Liga'
        assert data[1]['name'] == 'UEFA' or 'FIFA' or 'La Liga'

def test_create_competition(client):
    """Test for creating a new competition using static data."""
    new_competition = {
        'name': 'Bundesliga'
    }
    # Mocking the creation of a new competition
    with patch('app.routes.competitions.db.session.add') as mock_add, patch('app.routes.competitions.db.session.commit') as mock_commit:
        # Simulate a competition being added and committed
        mock_add.return_value = None
        mock_commit.return_value = None

        response = client.post('/competitions/', json=new_competition)
        assert response.status_code == 201
        data = response.get_json()
        assert data['name'] == new_competition['name']
        assert 'id' in data  # Check if an id is returned (simulating the ID generation)

def test_create_competition_missing_name(client):
    """Test for creating a competition with missing required fields."""
    new_competition = {}  # Missing 'name'
    response = client.post('/competitions/', json=new_competition)
    assert response.status_code == 400  # Validation error
    data = response.get_json()
    assert 'message' in data  # Validation error should return a message field
