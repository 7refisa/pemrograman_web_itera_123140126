/**
 * Kelas ScheduleItem merepresentasikan satu item jadwal.
 * Properti courseCode telah dihapus.
 */
class ScheduleItem {
  constructor(id, day, courseName, location, time) {
    this.id = id || Date.now().toString(); // Beri ID unik jika baru
    this.day = day;
    this.courseName = courseName;
    this.location = location;
    this.time = time;
  }
}

/**
 * Kelas utama ScheduleApp untuk mengelola seluruh logika aplikasi.
 */
class ScheduleApp {
  constructor() {
    // Gunakan 'const' untuk elemen DOM yang tidak akan berubah
    this.form = document.getElementById("schedule-form");
    this.submitButton = document.getElementById("form-submit-btn");
    this.cancelButton = document.getElementById("cancel-edit-btn");
    this.editIdInput = document.getElementById("edit-id");
    this.boardContainer = document.querySelector(".board-container");

    // Gunakan 'let' untuk data yang akan berubah
    this.items = []; // Menyimpan semua instance ScheduleItem
  }

  /**
   * Inisialisasi aplikasi.
   * Menggunakan Async Await untuk memuat data dari localStorage.
   */
  async init() {
    console.log("Aplikasi diinisialisasi...");
    // Memuat data secara asinkron
    const dataFromStorage = await this.fetchDataFromStorage();
    // Ubah data mentah menjadi instance Class
    this.items = dataFromStorage.map(
      (item) =>
        new ScheduleItem(
          item.id,
          item.day,
          item.courseName,
          item.location,
          item.time
        )
    );

    this.renderItems();
    this.addEventListeners();
  }

  /**
   * [Implementasi Fungsi Asinkron - Promise]
   * Mengambil data dari localStorage.
   */
  fetchDataFromStorage() {
    console.log("Mengambil data dari storage...");
    return new Promise((resolve) => {
      setTimeout(() => {
        const itemsJson = localStorage.getItem("scheduleItems") || "[]";
        const itemsArray = JSON.parse(itemsJson);
        console.log("Data berhasil diambil.");
        resolve(itemsArray);
      }, 500);
    });
  }

  /**
   * Menyimpan array 'items' saat ini ke localStorage.
   */
  saveToStorage() {
    localStorage.setItem("scheduleItems", JSON.stringify(this.items));
    console.log("Data disimpan ke localStorage.");
  }

  /**
   * Menambahkan semua event listener yang diperlukan.
   */
  addEventListeners() {
    this.form.addEventListener("submit", (e) => {
      e.preventDefault();
      this.handleSubmit();
    });

    this.boardContainer.addEventListener("click", (e) => {
      if (e.target.classList.contains("btn-delete")) {
        const card = e.target.closest(".class-card");
        const id = card.dataset.id;
        this.deleteItem(id);
      } else if (e.target.classList.contains("btn-edit")) {
        const card = e.target.closest(".class-card");
        const id = card.dataset.id;
        this.handleEdit(id);
      }
    });

    this.cancelButton.addEventListener("click", () => {
      this.resetForm();
    });
  }

  /**
   * Menangani logika submit form.
   */
  handleSubmit() {
    // Mengambil nilai dari form
    const day = this.form.day.value;
    const courseName = this.form.courseName.value;
    const location = this.form.location.value;
    const time = this.form.time.value;
    const editingId = this.editIdInput.value;

    if (editingId) {
      // Mode Update
      this.updateItem(editingId, day, courseName, location, time);
    } else {
      // Mode Tambah
      const newItem = new ScheduleItem(null, day, courseName, location, time);
      this.addItem(newItem);
    }

    this.resetForm();
  }

  /**
   * Menambahkan item baru ke array 'items' dan me-render ulang.
   */
  addItem(item) {
    this.items.push(item);
    this.saveToStorage();
    this.renderItems();
  }

  /**
   * Memperbarui item yang ada berdasarkan ID.
   */
  updateItem(id, day, courseName, location, time) {
    // Cari item berdasarkan ID
    const itemToUpdate = this.items.find((item) => item.id === id);
    if (itemToUpdate) {
      // Perbarui propertinya
      itemToUpdate.day = day;
      itemToUpdate.courseName = courseName;
      itemToUpdate.location = location;
      itemToUpdate.time = time;

      this.saveToStorage();
      this.renderItems();
      console.log(`Item ${id} diperbarui.`);
    }
  }

  /**
   * Menghapus item dari array 'items' berdasarkan ID.
   */
  deleteItem(id) {
    if (confirm("Apakah Anda yakin ingin menghapus jadwal ini?")) {
      this.items = this.items.filter((item) => item.id !== id);
      this.saveToStorage();
      this.renderItems();
      console.log(`Item ${id} dihapus.`);
    }
  }

  /**
   * Menyiapkan form untuk mode edit.
   */
  handleEdit(id) {
    const itemToEdit = this.items.find((item) => item.id === id);
    if (!itemToEdit) return;

    // Isi form dengan data item
    this.form.day.value = itemToEdit.day;
    this.form.courseName.value = itemToEdit.courseName;
    this.form.location.value = itemToEdit.location;
    this.form.time.value = itemToEdit.time;
    this.editIdInput.value = itemToEdit.id;

    // Ubah teks tombol dan tampilkan 'Batal'
    this.submitButton.innerText = "Update Jadwal";
    this.cancelButton.classList.remove("hidden");

    this.form.scrollIntoView({ behavior: "smooth" });
  }

  /**
   * Merender semua item ke kolom hari yang sesuai.
   */
  renderItems() {
    const containers = document.querySelectorAll(".cards-container");
    containers.forEach((container) => (container.innerHTML = ""));

    this.items.forEach((item) => {
      const container = document.getElementById(item.day);
      if (container) {
        // [Implementasi Template Literals]
        const cardHTML = `
                    <div class="class-card" data-id="${item.id}">
                        <h3>${item.courseName}</h3>
                        <p>${item.location}</p>
                        <p class="card-time">${item.time}</p>
                        <div class="card-actions">
                            <button class="btn-edit">Edit</button>
                            <button class="btn-delete">Hapus</button>
                        </div>
                    </div>
                `;
        container.insertAdjacentHTML("beforeend", cardHTML);
      }
    });
  }

  /**
   * Mengatur ulang (mereset) form ke keadaan default.
   */
  resetForm() {
    this.form.reset();
    this.editIdInput.value = "";
    this.submitButton.innerText = "Tambah Jadwal";
    this.cancelButton.classList.add("hidden");
  }
}

// Titik masuk utama aplikasi.
document.addEventListener("DOMContentLoaded", () => {
  const app = new ScheduleApp();
  app.init(); // Mulai aplikasi
});
