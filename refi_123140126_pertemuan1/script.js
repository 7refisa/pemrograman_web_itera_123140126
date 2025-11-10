document.addEventListener("DOMContentLoaded", () => {
  const taskForm = document.getElementById("task-form");
  const taskNameInput = document.getElementById("task-name");
  const taskSubjectInput = document.getElementById("task-subject");
  const taskDeadlineInput = document.getElementById("task-deadline");
  const taskListContainer = document.getElementById("task-list-container");
  const incompleteCountSpan = document.getElementById("incomplete-count");
  const searchInput = document.getElementById("search-input");
  const statusFilter = document.getElementById("status-filter");

  // Tombol baru untuk edit mode
  const addTaskBtn = document.getElementById("add-task-btn");
  const updateTaskBtn = document.getElementById("update-task-btn");
  const cancelEditBtn = document.getElementById("cancel-edit-btn");

  let tasks = JSON.parse(localStorage.getItem("tasks")) || [];
  let editingTaskId = null; // Menyimpan ID tugas yang sedang diedit

  const saveTasks = () => {
    localStorage.setItem("tasks", JSON.stringify(tasks));
  };

  const renderTasks = () => {
    taskListContainer.innerHTML = "";

    const filteredByStatus = tasks.filter((task) => {
      if (statusFilter.value === "all") return true;
      if (statusFilter.value === "completed") return task.completed;
      if (statusFilter.value === "incomplete") return !task.completed;
    });

    const searchQuery = searchInput.value.toLowerCase();
    const finalFilteredTasks = filteredByStatus.filter(
      (task) =>
        task.subject.toLowerCase().includes(searchQuery) ||
        task.name.toLowerCase().includes(searchQuery) // Tambahkan pencarian berdasarkan nama tugas juga
    );

    if (finalFilteredTasks.length === 0) {
      taskListContainer.innerHTML =
        '<p style="text-align:center; color:#888;">Tidak ada tugas yang sesuai.</p>';
    } else {
      finalFilteredTasks.forEach((task) => {
        const taskItem = document.createElement("div");
        taskItem.classList.add("task-item");
        if (task.completed) {
          taskItem.classList.add("completed");
        }

        taskItem.innerHTML = `
                    <div class="task-details">
                        <p class="task-name">${task.name}</p>
                        <p class="task-subject">${task.subject}</p>
                        <p class="task-deadline">Deadline: ${task.deadline}</p>
                    </div>
                    <div class="task-actions">
                        <button class="btn btn-complete" data-id="${task.id}">${
          task.completed ? "Batal" : "Selesai"
        }</button>
                        <button class="btn btn-edit" data-id="${
                          task.id
                        }">Edit</button> <button class="btn btn-delete" data-id="${
          task.id
        }">Hapus</button>
                    </div>
                `;
        taskListContainer.appendChild(taskItem);
      });
    }
    updateIncompleteCount();
  };

  const updateIncompleteCount = () => {
    const incompleteTasks = tasks.filter((task) => !task.completed).length;
    incompleteCountSpan.textContent = incompleteTasks;
  };

  // Fungsi untuk mengaktifkan mode edit
  const enableEditMode = (task) => {
    taskNameInput.value = task.name;
    taskSubjectInput.value = task.subject;
    taskDeadlineInput.value = task.deadline; // Pastikan format tanggal cocok dengan input type="date"
    editingTaskId = task.id;

    addTaskBtn.style.display = "none";
    updateTaskBtn.style.display = "inline-block";
    cancelEditBtn.style.display = "inline-block";
  };

  // Fungsi untuk menonaktifkan mode edit dan mereset form
  const disableEditMode = () => {
    taskForm.reset();
    editingTaskId = null;

    addTaskBtn.style.display = "inline-block";
    updateTaskBtn.style.display = "none";
    cancelEditBtn.style.display = "none";
  };

  // Event listener untuk form penambahan/pembaruan tugas
  taskForm.addEventListener("submit", (e) => {
    e.preventDefault();

    const taskName = taskNameInput.value.trim();
    const taskSubject = taskSubjectInput.value.trim();
    const taskDeadline = taskDeadlineInput.value;

    if (!taskName || !taskSubject || !taskDeadline) {
      alert("Semua field wajib diisi!");
      return;
    }

    if (editingTaskId) {
      // Mode Edit
      const taskIndex = tasks.findIndex((t) => t.id == editingTaskId);
      if (taskIndex !== -1) {
        tasks[taskIndex].name = taskName;
        tasks[taskIndex].subject = taskSubject;
        tasks[taskIndex].deadline = taskDeadline;
        saveTasks();
        renderTasks();
        disableEditMode();
      }
    } else {
      // Mode Tambah Tugas Baru
      const newTask = {
        id: Date.now(),
        name: taskName,
        subject: taskSubject,
        deadline: taskDeadline,
        completed: false,
      };

      tasks.push(newTask);
      saveTasks();
      renderTasks();
      taskForm.reset();
    }
  });

  // Event listener untuk tombol Update Tugas (jika di klik terpisah)
  updateTaskBtn.addEventListener("click", (e) => {});

  // Event listener untuk tombol Batal Edit
  cancelEditBtn.addEventListener("click", disableEditMode);

  // Event listener untuk tombol aksi (Selesai/Hapus/Edit)
  taskListContainer.addEventListener("click", (e) => {
    const target = e.target;
    const taskId = target.dataset.id;

    if (target.classList.contains("btn-complete")) {
      const task = tasks.find((t) => t.id == taskId);
      if (task) {
        task.completed = !task.completed;
        saveTasks();
        renderTasks();
      }
    }

    if (target.classList.contains("btn-delete")) {
      if (confirm("Apakah Anda yakin ingin menghapus tugas ini?")) {
        tasks = tasks.filter((t) => t.id != taskId);
        saveTasks();
        renderTasks();
        if (editingTaskId == taskId) {
          // Jika tugas yang dihapus sedang diedit
          disableEditMode();
        }
      }
    }

    if (target.classList.contains("btn-edit")) {
      // Event untuk tombol Edit
      const taskToEdit = tasks.find((t) => t.id == taskId);
      if (taskToEdit) {
        enableEditMode(taskToEdit);
      }
    }
  });

  // Event listener untuk filter dan pencarian
  searchInput.addEventListener("input", renderTasks);
  statusFilter.addEventListener("change", renderTasks);

  // Render tugas saat halaman pertama kali dimuat
  renderTasks();
});
