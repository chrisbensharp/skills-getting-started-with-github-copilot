"""Integration tests for API routes using AAA pattern."""


def test_get_activities(client):
    """Test GET /activities returns all activities."""
    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert len(data) == 9  # Based on current activities
    assert "Chess Club" in data
    assert "description" in data["Chess Club"]
    assert "schedule" in data["Chess Club"]
    assert "max_participants" in data["Chess Club"]
    assert "participants" in data["Chess Club"]
    assert isinstance(data["Chess Club"]["participants"], list)


def test_signup_success(client):
    """Test successful signup for an activity."""
    # Arrange
    activity_name = "Chess Club"
    email = "newstudent@mergington.edu"

    # Act
    response = client.post(f"/activities/{activity_name}/signup", json={"email": email})

    # Assert
    assert response.status_code == 200
    assert response.json() == {"message": f"Signed up {email} for {activity_name}"}


def test_signup_duplicate(client):
    """Test signup fails when student is already signed up."""
    # Arrange
    activity_name = "Chess Club"
    email = "michael@mergington.edu"  # Already in participants

    # Act
    response = client.post(f"/activities/{activity_name}/signup", json={"email": email})

    # Assert
    assert response.status_code == 400
    assert response.json() == {"detail": "Student already signed up"}


def test_signup_nonexistent_activity(client):
    """Test signup fails for non-existent activity."""
    # Arrange
    activity_name = "Nonexistent Activity"
    email = "test@mergington.edu"

    # Act
    response = client.post(f"/activities/{activity_name}/signup", json={"email": email})

    # Assert
    assert response.status_code == 404
    assert response.json() == {"detail": "Activity not found"}


def test_unregister_success(client):
    """Test successful unregister from an activity."""
    # Arrange
    activity_name = "Chess Club"
    email = "daniel@mergington.edu"  # Already in participants

    # Act
    response = client.delete(f"/activities/{activity_name}/signup", json={"email": email})

    # Assert
    assert response.status_code == 200
    assert response.json() == {"message": f"Unregistered {email} from {activity_name}"}


def test_unregister_not_signed_up(client):
    """Test unregister fails when student is not signed up."""
    # Arrange
    activity_name = "Chess Club"
    email = "notsigned@mergington.edu"

    # Act
    response = client.delete(f"/activities/{activity_name}/signup", json={"email": email})

    # Assert
    assert response.status_code == 400
    assert response.json() == {"detail": "Student not signed up for this activity"}


def test_unregister_nonexistent_activity(client):
    """Test unregister fails for non-existent activity."""
    # Arrange
    activity_name = "Nonexistent Activity"
    email = "test@mergington.edu"

    # Act
    response = client.delete(f"/activities/{activity_name}/signup", json={"email": email})

    # Assert
    assert response.status_code == 404
    assert response.json() == {"detail": "Activity not found"}