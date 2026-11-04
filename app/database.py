"""Small SQLite helpers used by the To-Do API."""

from contextlib import contextmanager
from pathlib import Path
import sqlite3
from typing import Iterator


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_DATABASE_PATH = PROJECT_ROOT / "data" / "todo.db"


@contextmanager
def get_connection(database_path: Path) -> Iterator[sqlite3.Connection]:
    """Open a SQLite connection and always close it when the request ends."""
    connection = sqlite3.connect(database_path)
    connection.row_factory = sqlite3.Row
    try:
        yield connection
    finally:
        connection.close()


def initialize_database(database_path: Path = DEFAULT_DATABASE_PATH) -> None:
    """Create the database folder and tasks table if they do not exist yet."""
    database_path.parent.mkdir(parents=True, exist_ok=True)
    with get_connection(database_path) as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                is_completed INTEGER NOT NULL DEFAULT 0,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL
            )
            """
        )
        connection.commit()
