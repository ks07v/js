from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_chat():
    resp = client.post("/v1/chat", json={"user_id": "user1", "message": "넷플릭스 해지할까?"})
    assert resp.status_code == 200
    data = resp.json()
    assert data["intent"] == "SUB_CANCEL"


def test_subscription():
    resp = client.get("/v1/subscription/user1")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, list)


def test_feedback():
    resp = client.post("/v1/feedback", json={"chat_id": "1", "rating": 5})
    assert resp.status_code == 200
    assert resp.json()["status"] == "ok"
