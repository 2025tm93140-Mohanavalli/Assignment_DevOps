from app import app


def test_home():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert response.json["status"] == "Application is running"


def test_health():
    client = app.test_client()
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json["status"] == "healthy"


def test_workouts():
    client = app.test_client()
    response = client.get("/workouts")

    assert response.status_code == 200
    assert "workouts" in response.json
    assert len(response.json["workouts"]) > 0