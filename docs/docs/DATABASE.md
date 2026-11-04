# Database — Basic To-Do Application

**Document ID:** DATA-001  
**Status:** Proposed

## 1. Database choice

Use SQLite for the initial version. SQLite stores data in a local file and does not require a separately installed or running database server.

Proposed database filename: `todo.db` (location to be finalized during implementation; keep it outside public static files).

## 2. Initial table

### `tasks`

| Column | Type | Rules | Description |
|---|---|---|---|
| `id` | INTEGER | Primary key; auto-increment | Unique task identifier |
| `title` | TEXT | Not null | Task description |
| `is_completed` | INTEGER | Not null; default `0` | `0` = incomplete, `1` = complete |
| `created_at` | TEXT | Not null | Creation timestamp in ISO 8601 format |
| `updated_at` | TEXT | Not null | Last update timestamp in ISO 8601 format |

## 3. Conceptual SQL

```sql
CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    is_completed INTEGER NOT NULL DEFAULT 0,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL
);
```

This is a proposed schema. The implementation should also enforce non-empty trimmed titles in application validation.

## 4. Data behavior

- Adding a task sets `is_completed` to `0`.
- Editing a task updates `title` and `updated_at`.
- Completing or reopening a task updates `is_completed` and `updated_at`.
- Deleting a task removes its row.
- Listing tasks should use a deterministic order; proposed default is newest first (`created_at` descending, then `id` descending).

## 5. Data access and safety

- Use parameterized SQL queries; never concatenate user-provided values into SQL statements.
- Close database connections reliably.
- Do not place the database file in a publicly served static directory.
- Database schema creation should be repeatable and safe when the application starts.
- A formal migration tool is not required for the first tiny version; revisit if schema changes become frequent.

## 6. Open decisions

- Final database file location.
- Maximum task-title length.
- Whether timestamps are stored in UTC (recommended) and formatted for display in the browser's local time.
