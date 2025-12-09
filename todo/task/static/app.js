const API = "/u/tasks/";

async function loadTasks() {
    const res = await fetch(API);
    const tasks = await res.json();

    let html = "";
    tasks.forEach(t => {
        html += `
            <div class="col-md-4">
                <div class="p-3 border rounded shadow-sm">
                    <h5>${t.title}</h5>
                    <p>${t.description}</p>
                    <span class="badge bg-info">${t.status}</span>

                    <div class="mt-2">
                        <button class="btn btn-warning btn-sm" onclick="openEdit(${t.id})">Edit</button>
                        <button class="btn btn-danger btn-sm" onclick="delTask(${t.id})">Delete</button>
                    </div>
                </div>
            </div>
        `;
    });

    document.getElementById("taskList").innerHTML = html;
}

loadTasks();

// ADD
function openAdd() {
    document.getElementById("modalTitle").innerText = "Add Task";
    document.getElementById("taskId").value = "";
    document.getElementById("title").value = "";
    document.getElementById("description").value = "";
    document.getElementById("status").value = "Pending";
}

// EDIT
async function openEdit(id) {
    const res = await fetch(API + id + "/");
    const t = await res.json();

    document.getElementById("modalTitle").innerText = "Edit Task";
    document.getElementById("taskId").value = t.id;
    document.getElementById("title").value = t.title;
    document.getElementById("description").value = t.description;
    document.getElementById("status").value = t.status;

    new bootstrap.Modal(document.getElementById("taskModal")).show();
}

// SAVE (ADD or EDIT)
async function saveTask() {
    let id = document.getElementById("taskId").value;

    let data = {
        title: document.getElementById("title").value,
        description: document.getElementById("description").value,
        status: document.getElementById("status").value,
    };

    let method = id ? "PATCH" : "POST";
    let url = id ? API + id + "/" : API;

    await fetch(url, {
        method: method,
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
    });

    loadTasks();
    bootstrap.Modal.getInstance(document.getElementById("taskModal")).hide();
}

// DELETE
async function delTask(id) {
    if (!confirm("Delete this task?")) return;

    await fetch(API + id + "/", { method: "DELETE" });
    loadTasks();
}
