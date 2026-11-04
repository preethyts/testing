# Development Guide — Basic To-Do Application

**Document ID:** DEV-001  
**Status:** Proposed local setup

## 1. Prerequisites

- Python 3.11 or a compatible newer version.
- Git.
- A code editor.
- A modern web browser.

A virtual environment is recommended so project dependencies remain isolated.

## 2. Proposed dependencies

The initial backend dependency is:

- `fastapi`
- `uvicorn[standard]`

Python's built-in `sqlite3` module is sufficient for the proposed simple database access, so a separate ORM is not required initially.

Exact dependency versions should be selected and pinned when implementation begins.

## 3. Local setup outline

From the project root:

```bash
# Create a virtual environment
python -m venv .venv

# Activate on Windows PowerShell
.venv\Scripts\Activate.ps1

# Activate on macOS/Linux
source .venv/bin/activate

# Install dependencies after creating requirements.txt
pip install -r requirements.txt
```

## 4. Run the application

The proposed development command, once `app/main.py` exists:

```bash
uvicorn app.main:app --reload
```

Then open:

- Application: `http://127.0.0.1:8000`
- FastAPI interactive API documentation: `http://127.0.0.1:8000/docs`

These URLs assume the proposed local development configuration.

## 5. Git basics

Typical workflow:

```bash
git init
git status
git add .
git commit -m "Initial project setup"
```

Do not commit `.venv/`, local database files, secrets, or machine-specific files. Add appropriate entries to `.gitignore`.

## 6. Suggested learning sequence

1. Understand the folder structure and how FastAPI starts.
2. Start the server and open the browser page.
3. Understand one API endpoint from browser to backend.
4. Add SQLite persistence.
5. Implement create and list.
6. Implement edit and completion.
7. Implement delete.
8. Add basic tests and verify acceptance criteria.
9. Review the changes and commit them with Git.

## 7. Troubleshooting starting points

- If `uvicorn` is not found, confirm the virtual environment is activated and dependencies are installed.
- If the module cannot be imported, check the working directory and Python package structure.
- If the database cannot be opened, check the configured file path and folder permissions.
- If browser requests fail, inspect the browser developer console and the FastAPI terminal output.

## 8. Important note

This guide documents a proposed setup. No setup commands have been executed and no application has been built as part of this documentation package.
