from fastapi.testclient import TestClient

from src.app import app


def test_get_activities_returns_activity_list():
    client = TestClient(app)

    response = client.get("/activities")

    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert "Chess Club" in response.json()


def test_signup_for_activity_adds_participant():
    client = TestClient(app)
    email = "newstudent@mergington.edu"
    activity_name = "Chess Club"

    response = client.post(f"/activities/{activity_name}/signup?email={email}")

    assert response.status_code == 200
    assert response.json()["message"] == f"Signed up {email} for {activity_name}"

    # Verify the participant was added in the returned activity list
    activity_response = client.get("/activities")
    assert email in activity_response.json()[activity_name]["participants"]


def test_signup_duplicate_participant_returns_400():
    client = TestClient(app)
    existing_email = "michael@mergington.edu"
    activity_name = "Chess Club"

    response = client.post(f"/activities/{activity_name}/signup?email={existing_email}")

    assert response.status_code == 400
    assert response.json()["detail"] == "Student is already signed up for this activity"


def test_signup_unknown_activity_returns_404():
    client = TestClient(app)
    email = "student@mergington.edu"
    activity_name = "Unknown Club"

    response = client.post(f"/activities/{activity_name}/signup?email={email}")

    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"
