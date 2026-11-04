# Basic To-Do Application

**Project status:** Initial documentation baseline  
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

These are the proposed choices for the learning project, not evidence of an implemented system. The database access approach can be revisited if the project grows.

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

This is a suggested structure only. No application files or implementation are included in this documentation package.

## 5. Documentation

Start with the documents in `docs/`:

- [Requirements](docs/REQUIREMENTS.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Database](docs/DATABASE.md)
- [API](docs/API.md)
- [Development guide](docs/DEVELOPMENT_GUIDE.md)
- [Codex instructions](docs/CODEX_INSTRUCTIONS.md)

## 6. Current state

- Requirements and technical design are documented at an introductory level.
- Technology choices are proposed for a simple learning implementation.
- No application code has been written.
- No dependencies have been installed.
- No tests or builds have been run.
- Implementation requires separate authorization.
