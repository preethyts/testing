# Basic To-Do Application

**Project status:** Implemented local learning application
**Scope:** A small browser-based To-Do application for learning AI-assisted software development.

## 1. Overview

The application lets a user create, view, edit, complete, and delete tasks through a simple web page.

It is intentionally small. The first version does not include user accounts, authentication, cloud hosting, dashboards, notifications, or a frontend framework.

## 2. Proposed technology stack

| Layer | Proposed technology |
|---|---|
| Browser UI | HTML, CSS, vanilla JavaScript |
| Backend | Python with FastAPI |
| Database | SQLite |
| Database access | Python's built-in `sqlite3` module (minimal starting choice) |
| Version control | Git |
| AI development workflow | ChatGPT for planning/review; Codex for repository coding tasks |

These choices are implemented for the first version. The database access approach can be revisited if the project grows.

## 3. Main features

1. Add a task.
2. View all tasks.
3. Edit a task.
4. Mark a task as completed or incomplete.
5. Delete a task.

## 4. Suggested project structure

```text
basic-todo/
├── app/
│   ├── main.py
│   ├── database.py
│   ├── templates/
│   │   └── index.html
│   └── static/
│       ├── styles.css
│       └── app.js
├── requirements.txt
├── README.md
└── docs/
    ├── REQUIREMENTS.md
    ├── ARCHITECTURE.md
    ├── DATABASE.md
    ├── API.md
    ├── DEVELOPMENT_GUIDE.md
    └── CODEX_INSTRUCTIONS.md
```

The implementation also includes `tests/test_api.py` for API coverage and a local `data/` directory that is created automatically for the SQLite database. The database itself is ignored by Git.

## 5. Documentation

Start with the documents in `docs/`:

- [Requirements](docs/REQUIREMENTS.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Database](docs/DATABASE.md)
- [API](docs/API.md)
- [Development guide](docs/DEVELOPMENT_GUIDE.md)
- [Codex instructions](docs/CODEX_INSTRUCTIONS.md)

## 6. Run locally (Windows PowerShell)

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open the application at `http://127.0.0.1:8000` and FastAPI's Swagger interface at `http://127.0.0.1:8000/docs`.

Run the automated API tests with `pytest`.

## 7. Implementation decisions

- Task titles are trimmed, required, and limited to 200 characters.
- Tasks are displayed newest first; completed tasks stay in the same list with a struck-through appearance.
- SQLite data is stored in `data/todo.db`, outside the public static folder, with UTC ISO 8601 timestamps.
