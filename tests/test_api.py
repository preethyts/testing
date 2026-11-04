from pathlib import Path
import pytest
from fastapi.testclient import TestClient
from app.database import initialize_database
from app.main import app

@pytest.fixture()
def client(tmp_path: Path):
    database_path = tmp_path / "todo.db"; app.state.database_path = database_path; initialize_database(database_path)
    with TestClient(app) as test_client: yield test_client

def create_task(client: TestClient, title: str = "Buy milk") -> dict:
    response = client.post("/api/tasks", json={"title": title}); assert response.status_code == 201; return response.json()

def test_create_and_list_tasks_newest_first(client: TestClient):
    first = create_task(client, "First"); second = create_task(client, "Second"); response = client.get("/api/tasks")
    assert response.status_code == 200; assert [task["id"] for task in response.json()] == [second["id"], first["id"]]; assert second["is_completed"] is False; assert second["created_at"].endswith("Z")

def test_create_trims_unicode_and_allows_duplicates(client: TestClient):
    first = create_task(client, "  Plan café ☕!  "); second = create_task(client, "Plan café ☕!")
    assert first["title"] == "Plan café ☕!"; assert second["title"] == "Plan café ☕!"; assert first["id"] != second["id"]

@pytest.mark.parametrize("title", ["", "   ", "\t\n"])
def test_create_rejects_empty_titles(client: TestClient, title: str):
    response = client.post("/api/tasks", json={"title": title}); assert response.status_code == 422; assert response.json()["detail"] == "Task title cannot be empty."

def test_rejects_title_longer_than_200_characters(client: TestClient):
    response = client.post("/api/tasks", json={"title": "a" * 201}); assert response.status_code == 422; assert "200 characters" in response.json()["detail"]

def test_edit_task(client: TestClient):
    task = create_task(client); response = client.put(f"/api/tasks/{task['id']}", json={"title": "Buy oat milk"}); assert response.status_code == 200; assert response.json()["title"] == "Buy oat milk"

def test_complete_and_reopen_task(client: TestClient):
    task = create_task(client); completed = client.patch(f"/api/tasks/{task['id']}/completion", json={"is_completed": True}); reopened = client.patch(f"/api/tasks/{task['id']}/completion", json={"is_completed": False})
    assert completed.status_code == 200; assert completed.json()["is_completed"] is True; assert reopened.status_code == 200; assert reopened.json()["is_completed"] is False

def test_delete_task(client: TestClient):
    task = create_task(client); response = client.delete(f"/api/tasks/{task['id']}"); assert response.status_code == 204; assert client.get("/api/tasks").json() == []

@pytest.mark.parametrize(("method", "url", "payload"), [("put", "/api/tasks/999", {"title": "Missing"}), ("patch", "/api/tasks/999/completion", {"is_completed": True}), ("delete", "/api/tasks/999", None)])
def test_unknown_task_returns_not_found(client: TestClient, method: str, url: str, payload: dict | None):
    request = getattr(client, method)
    response = request(url) if payload is None else request(url, json=payload)
    assert response.status_code == 404; assert response.json()["detail"] == "Task not found."

def test_data_persists_when_database_is_reopened(tmp_path: Path):
    database_path = tmp_path / "persistent.db"; app.state.database_path = database_path; initialize_database(database_path)
    with TestClient(app) as first_client: create_task(first_client, "Persist me")
    with TestClient(app) as restarted_client: tasks = restarted_client.get("/api/tasks").json()
    assert [task["title"] for task in tasks] == ["Persist me"]
