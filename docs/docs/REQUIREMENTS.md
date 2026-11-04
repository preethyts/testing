# Requirements — Basic To-Do Application

**Document ID:** REQ-001  
**Status:** Initial baseline  
**Scope:** First, deliberately minimal version

## 1. Purpose

Provide a simple browser-based task list. The project is also intended as a learning exercise for understanding how ChatGPT, Codex, Git, a backend API, and a database fit into an AI-assisted development workflow.

## 2. Users and operating assumptions

- The first version is for a single local user.
- The application is accessed through a web browser.
- The application is expected to run locally during initial development.
- Authentication and multiple-user support are outside the initial scope.

## 3. Functional requirements

| ID | Requirement | Expected behavior |
|---|---|---|
| FR-001 | Add task | User can enter a task title and save it. |
| FR-002 | List tasks | User can view saved tasks. |
| FR-003 | Edit task | User can change the title of an existing task. |
| FR-004 | Complete task | User can mark a task completed or incomplete. |
| FR-005 | Delete task | User can delete an existing task. |

## 4. Basic validation

- A task title must not be empty or consist only of whitespace.
- The backend must validate input; browser-side validation alone is insufficient.
- An operation targeting a task that does not exist should return an appropriate not-found response.
- Invalid input should return a clear client error.

A maximum task-title length is **TBD** and should be agreed before implementation.

## 5. Non-functional requirements

- Keep the application small and easy to understand.
- Use plain HTML, CSS, and vanilla JavaScript; no React or other frontend framework.
- Use FastAPI for the Python backend.
- Use a lightweight local database; SQLite is the proposed choice.
- Keep secrets and environment-specific configuration out of source control.
- Return understandable errors rather than exposing internal stack traces to the browser.

Specific performance, availability, accessibility, and security targets are not defined for this local learning version.

## 6. Out of scope

- Login, registration, roles, and permissions.
- Multiple users or shared task lists.
- Categories, tags, priorities, due dates, reminders, and recurring tasks.
- File attachments.
- Mobile application.
- Cloud deployment and production operations.
- Third-party integrations.

## 7. Acceptance criteria

- A user can add a task and see it in the list.
- A saved task remains available after restarting the application.
- A user can edit a task title and see the updated title.
- A user can toggle a task between completed and incomplete.
- A user can delete a task and it no longer appears in the list.
- Empty task titles are rejected by the backend.
- Unknown task IDs produce a not-found response.

## 8. Open decisions

- Maximum allowed task-title length.
- Whether completed tasks appear in the same list or a separate section. Initial recommendation: same list, visually distinguished.
- Whether task ordering is oldest-first or newest-first. Initial recommendation: newest-first.
