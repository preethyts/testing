"""FastAPI application for the basic local To-Do app."""

from datetime import datetime, timezone
from pathlib import Path
import logging
import sqlite3

from fastapi import FastAPI, HTTPException, Request, status
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from .database import DEFAULT_DATABASE_PATH, get_connection, initialize_database


logger = logging.getLogger(__name__)
MAX_TITLE_LENGTH = 200
APP_DIRECTORY = Path(__file__).resolve().parent

app = FastAPI(title="Basic To-Do Application")
app.state.database_path = DEFAULT_DATABASE_PATH
app.mount("/static", StaticFiles(directory=APP_DIRECTORY / "static"), name="static")


class TaskInput(BaseModel):
    title: str


class CompletionInput(BaseModel):
    is_completed: bool


def utc_now() -> str:
    """Return an ISO 8601 UTC timestamp that ends in Z."""
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def clean_title(title: str) -> str:
    """Trim and validate a task title shared by create and edit operations."""
    cleaned_title = title.strip()
    if not cleaned_title:
        raise HTTPException(status_code=422, detail="Task title cannot be empty.")
    if len(cleaned_title) > MAX_TITLE_LENGTH:
        raise HTTPException(
            status_code=422,
            detail=f"Task title must be {MAX_TITLE_LENGTH} characters or fewer.",
        )
    return cleaned_title


def task_to_dict(row: sqlite3.Row) -> dict:
    return {
        "id": row["id"], "title": row["title"],
        "is_completed": bool(row["is_completed"]),
        "created_at": row["created_at"], "updated_at": row["updated_at"],
    }


def fetch_task(connection: sqlite3.Connection, task_id: int) -> sqlite3.Row:
    task = connection.execute("SELECT * FROM tasks WHERE id = ?", (task_id,)).fetchone()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found.")
    return task


@app.on_event("startup")
def start_database() -> None:
    initialize_database(app.state.database_path)


@app.exception_handler(sqlite3.Error)
async def database_error_handler(_: Request, error: sqlite3.Error) -> JSONResponse:
    """Keep SQLite implementation details out of browser responses."""
    logger.exception("Database operation failed", exc_info=error)
    return JSONResponse(status_code=500, content={"detail": "A database error occurred. Please try again."})


@app.get("/", include_in_schema=False)
async def home() -> FileResponse:
    return FileResponse(APP_DIRECTORY / "templates" / "index.html")


@app.get("/api/tasks")
async def list_tasks() -> list[dict]:
    with get_connection(app.state.database_path) as connection:
        tasks = connection.execute("SELECT * FROM tasks ORDER BY created_at DESC, id DESC").fetchall()
    return [task_to_dict(task) for task in tasks]


@app.post("/api/tasks", status_code=status.HTTP_201_CREATED)
async def create_task(task_input: TaskInput) -> dict:
    title = clean_title(task_input.title)
    timestamp = utc_now()
    with get_connection(app.state.database_path) as connection:
        cursor = connection.execute(
            "INSERT INTO tasks (title, is_completed, created_at, updated_at) VALUES (?, ?, ?, ?)",
            (title, 0, timestamp, timestamp),
        )
        connection.commit()
        task = fetch_task(connection, cursor.lastrowid)
    return task_to_dict(task)


@app.put("/api/tasks/{task_id}")
async def update_task(task_id: int, task_input: TaskInput) -> dict:
    title = clean_title(task_input.title)
    with get_connection(app.state.database_path) as connection:
        fetch_task(connection, task_id)
        connection.execute("UPDATE tasks SET title = ?, updated_at = ? WHERE id = ?", (title, utc_now(), task_id))
        connection.commit()
        task = fetch_task(connection, task_id)
    return task_to_dict(task)


@app.patch("/api/tasks/{task_id}/completion")
async def update_completion(task_id: int, completion_input: CompletionInput) -> dict:
    with get_connection(app.state.database_path) as connection:
        fetch_task(connection, task_id)
        connection.execute(
            "UPDATE tasks SET is_completed = ?, updated_at = ? WHERE id = ?",
            (int(completion_input.is_completed), utc_now(), task_id),
        )
        connection.commit()
        task = fetch_task(connection, task_id)
    return task_to_dict(task)


@app.delete("/api/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: int) -> None:
    with get_connection(app.state.database_path) as connection:
        fetch_task(connection, task_id)
        connection.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        connection.commit()
