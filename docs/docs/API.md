# API Specification — Basic To-Do Application

**Document ID:** API-001  
**Status:** Proposed initial contract  
**Base path:** `/api`

All request and response bodies use JSON unless stated otherwise.

## 1. Task representation

```json
{
  "id": 1,
  "title": "Read a chapter",
  "is_completed": false,
  "created_at": "2026-11-04T06:00:00Z",
  "updated_at": "2026-11-04T06:00:00Z"
}
```

Timestamps are illustrative. The implementation should use a consistent ISO 8601 representation.

## 2. Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/api/tasks` | Return all tasks |
| POST | `/api/tasks` | Create a task |
| PUT | `/api/tasks/{task_id}` | Update a task title |
| PATCH | `/api/tasks/{task_id}/completion` | Set completion state |
| DELETE | `/api/tasks/{task_id}` | Delete a task |

## 3. Request examples

### Create — `POST /api/tasks`

```json
{
  "title": "Read a chapter"
}
```

### Update title — `PUT /api/tasks/1`

```json
{
  "title": "Read two chapters"
}
```

### Set completion — `PATCH /api/tasks/1/completion`

```json
{
  "is_completed": true
}
```

The completion endpoint sets the requested state; it should not merely toggle blindly. This makes repeated requests predictable.

## 4. Response expectations

- `GET`: `200 OK` with an array of task objects.
- `POST`: `201 Created` with the created task.
- `PUT`: `200 OK` with the updated task.
- `PATCH`: `200 OK` with the updated task.
- `DELETE`: `204 No Content` after successful deletion.
- Invalid input: `422 Unprocessable Entity` or a consistently documented `400 Bad Request`.
- Unknown task ID: `404 Not Found`.

FastAPI may provide its standard validation response format. The frontend should handle unsuccessful responses and show a useful message.

## 5. Error response concept

```json
{
  "detail": "Task not found"
}
```

Exact error payloads should remain consistent across endpoints.

## 6. API documentation

FastAPI's automatically generated OpenAPI documentation can be used during development, normally at `/docs`. This is a development aid, not a separate application feature.
