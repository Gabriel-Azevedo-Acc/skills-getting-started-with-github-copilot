from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_get_activities():
    # Arrange: nothing to set up
    # Act
    response = client.get("/activities")
    # Assert
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_signup_activity():
    # Arrange
    activity = "Chess Club"
    email = "pytestuser@mergington.edu"
    # Act
    response = client.post(f"/activities/{activity}/signup?email={email}")
    # Assert
    assert response.status_code in (200, 400)
    data = response.json()
    assert "message" in data or "detail" in data
