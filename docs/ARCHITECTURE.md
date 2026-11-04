# Architecture — Basic To-Do Application

**Document ID:** ARC-001  
**Status:** Proposed

## 1. Architecture summary

A small, single-process web application:

```text
Browser
  ├── HTML page
  ├── CSS
  └── Vanilla JavaScript
          │ HTTP requests (JSON)
          ▼
Python FastAPI application
  ├── Serves the page and static assets
  ├── Exposes task API endpoints
  └── Validates requests and coordinates persistence
          │
          ▼
SQLite database file
```

## 2. Component responsibilities

### Browser UI

- Displays the task list and task-entry form.
- Sends HTTP requests to the backend using browser `fetch`.
- Updates the page based on API responses.
- Provides basic input feedback.
- Does not connect directly to the database.

### FastAPI backend

- Serves the HTML page and static CSS/JavaScript files.
- Exposes the task API described in `API.md`.
- Validates incoming data.
- Applies task operations and returns JSON responses.
- Handles missing records and invalid requests.

### SQLite

- Stores task records in a local database file.
- Persists data between application restarts.
- Does not require a separate database server.

## 3. Suggested implementation organization

- `main.py`: FastAPI application, page/static mounting, and route registration.
- `database.py`: SQLite connection and database initialization helpers.
- `templates/index.html`: Main page.
- `static/styles.css`: Basic styling.
- `static/app.js`: Browser interactions and API calls.

The exact organization may be adjusted during implementation if there is a clear simplicity or maintainability benefit.

## 4. Request flow: adding a task

1. User enters a title in the browser.
2. JavaScript sends a `POST /api/tasks` request with JSON.
3. FastAPI validates the title.
4. Backend inserts the task into SQLite.
5. Backend returns the created task as JSON.
6. Browser refreshes or updates the displayed list.

## 5. Design constraints

- No frontend framework.
- No separate database server.
- No microservices or background workers.
- No authentication in the initial version.
- Keep business logic and database access understandable and small.

## 6. Risks and limitations

- SQLite is suitable for this small local application; it may not be the right choice for a high-concurrency, multi-user hosted service.
- No authentication means the initial application should remain local or otherwise protected from untrusted access.
- Production deployment, backups, migrations, and operational monitoring are not specified.

## 7. Architecture decisions

The technology stack in this document is proposed, not yet verified through implementation. Any material change should be discussed and recorded before implementation.
