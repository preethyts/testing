# Codex Instructions — Basic To-Do Application

**Document ID:** AI-001  
**Status:** Initial agent guidance

## 1. Project purpose

This is a small browser-based To-Do application intended as a learning project for AI-assisted software development.

Read these documents before making changes:

1. `README.md`
2. `docs/REQUIREMENTS.md`
3. `docs/ARCHITECTURE.md`
4. `docs/DATABASE.md`
5. `docs/API.md`
6. `docs/DEVELOPMENT_GUIDE.md`

## 2. Technology constraints

- Backend: Python and FastAPI.
- Frontend: plain HTML, CSS, and vanilla JavaScript.
- Database: SQLite.
- Prefer Python's built-in `sqlite3` module for the initial implementation.
- Do not introduce React, Vue, Angular, a frontend build system, a separate database server, microservices, or unrelated infrastructure.

If a constraint appears unsuitable, explain why and ask before changing it.

## 3. Working rules

Before coding:

1. Inspect the existing repository and current Git state.
2. Read the relevant requirements and design documents.
3. Identify the files and behavior affected by the task.
4. Report missing or conflicting requirements before making assumptions.

While coding:

- Implement only the requested, agreed scope.
- Keep changes small and understandable for a beginner.
- Validate user input on the backend.
- Use parameterized SQL.
- Handle missing records and expected errors.
- Do not expose secrets or commit local database files.
- Avoid unrelated refactoring and new dependencies.

After coding:

1. Run relevant tests and report the exact commands and results.
2. Report tests that could not be run.
3. Summarize files created, changed, and removed.
4. Identify design decisions, limitations, and remaining work.
5. Update documentation if behavior, APIs, schema, or setup instructions changed.
6. Do not claim that unexecuted tests passed.

## 4. Scope control

The first version is limited to:

- Add task.
- List tasks.
- Edit task title.
- Mark task complete/incomplete.
- Delete task.

Do not add authentication, user accounts, task categories, reminders, priorities, due dates, cloud deployment, or other features unless explicitly requested.

## 5. Task prompt expectations

Each task supplied to Codex should state:

- Objective.
- Relevant requirement IDs.
- Files or areas to inspect.
- Included scope and out-of-scope items.
- Acceptance criteria.
- Tests to run.
- Required handover details.

## 6. Handover format

At the end of each task, report:

- Objective and requirement IDs.
- Work completed.
- Files created, modified, or deleted.
- Important implementation decisions.
- Tests run and their results.
- Tests not run and why.
- Any dependency or database changes.
- Known issues, deviations, and remaining work.
- Suggested next step.

A handover is a report, not proof by itself. The user or reviewer should inspect the repository and test evidence.

## 7. Authorization boundary

Documentation does not itself authorize implementation. Wait for the user's explicit instruction before creating or modifying application code.
