const taskForm = document.querySelector("#task-form");
const newTaskInput = document.querySelector("#new-task");
const addButton = document.querySelector("#add-button");
const taskList = document.querySelector("#task-list");
const feedback = document.querySelector("#feedback");
const loading = document.querySelector("#loading");
const emptyState = document.querySelector("#empty-state");

function showFeedback(message, type = "success") { feedback.textContent = message; feedback.className = `feedback ${type}`; }
function setLoading(isLoading) { loading.hidden = !isLoading; }

async function readResponse(response) {
  const body = await response.json().catch(() => ({}));
  if (!response.ok) throw new Error(body.detail || "Something went wrong. Please try again.");
  return body;
}
async function request(url, options = {}) {
  try { return await readResponse(await fetch(url, options)); }
  catch (error) { if (error instanceof TypeError) throw new Error("Unable to reach the server. Check that it is running and try again."); throw error; }
}
function makeButton(label, className, onClick) {
  const button = document.createElement("button"); button.type = "button"; button.textContent = label; button.className = className; button.addEventListener("click", onClick); return button;
}
function renderTasks(tasks) {
  taskList.replaceChildren(); emptyState.hidden = tasks.length !== 0;
  for (const task of tasks) {
    const item = document.createElement("li"); item.className = task.is_completed ? "task completed" : "task";
    const checkbox = document.createElement("input"); checkbox.type = "checkbox"; checkbox.checked = task.is_completed;
    checkbox.setAttribute("aria-label", `Mark ${task.title} as ${task.is_completed ? "incomplete" : "complete"}`);
    checkbox.addEventListener("change", () => changeCompletion(task.id, checkbox.checked));
    const title = document.createElement("span"); title.className = "task-title"; title.textContent = task.title;
    const actions = document.createElement("div"); actions.className = "task-actions";
    actions.append(makeButton("Edit", "secondary", () => editTask(task)), makeButton("Delete", "danger", () => removeTask(task)));
    item.append(checkbox, title, actions); taskList.append(item);
  }
}
async function loadTasks() {
  setLoading(true); try { renderTasks(await request("/api/tasks")); } catch (error) { showFeedback(error.message, "error"); } finally { setLoading(false); }
}
taskForm.addEventListener("submit", async (event) => {
  event.preventDefault(); const title = newTaskInput.value.trim();
  if (!title) { showFeedback("Please enter a task title.", "error"); newTaskInput.focus(); return; }
  addButton.disabled = true;
  try { await request("/api/tasks", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ title }) }); newTaskInput.value = ""; showFeedback("Task added."); await loadTasks(); newTaskInput.focus(); }
  catch (error) { showFeedback(error.message, "error"); } finally { addButton.disabled = false; }
});
async function editTask(task) {
  const title = window.prompt("Edit task title:", task.title); if (title === null) return;
  if (!title.trim()) { showFeedback("Please enter a task title.", "error"); return; }
  try { await request(`/api/tasks/${task.id}`, { method: "PUT", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ title }) }); showFeedback("Task updated."); await loadTasks(); }
  catch (error) { showFeedback(error.message, "error"); }
}
async function changeCompletion(id, isCompleted) {
  try { await request(`/api/tasks/${id}/completion`, { method: "PATCH", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ is_completed: isCompleted }) }); showFeedback(isCompleted ? "Task completed." : "Task reopened."); await loadTasks(); }
  catch (error) { showFeedback(error.message, "error"); await loadTasks(); }
}
async function removeTask(task) {
  if (!window.confirm(`Delete "${task.title}"?`)) return;
  try { await request(`/api/tasks/${task.id}`, { method: "DELETE" }); showFeedback("Task deleted."); await loadTasks(); }
  catch (error) { showFeedback(error.message, "error"); }
}
loadTasks();
