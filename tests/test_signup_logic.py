"""Unit tests for business logic using AAA pattern."""

from src.app import activities


def test_activities_data_structure():
    """Test that activities data has correct structure."""
    # Assert
    assert isinstance(activities, dict)
    assert len(activities) > 0

    for activity_name, activity_data in activities.items():
        assert isinstance(activity_name, str)
        assert "description" in activity_data
        assert "schedule" in activity_data
        assert "max_participants" in activity_data
        assert "participants" in activity_data
        assert isinstance(activity_data["participants"], list)
        assert isinstance(activity_data["max_participants"], int)
        assert activity_data["max_participants"] > 0


def test_participants_list_integrity():
    """Test that participants lists contain valid email-like strings."""
    # Assert
    for activity_data in activities.values():
        participants = activity_data["participants"]
        for email in participants:
            assert isinstance(email, str)
            assert "@" in email  # Basic email check


def test_max_participants_reasonable():
    """Test that max_participants are reasonable numbers."""
    # Assert
    for activity_data in activities.values():
        max_part = activity_data["max_participants"]
        assert 1 <= max_part <= 50  # Reasonable range