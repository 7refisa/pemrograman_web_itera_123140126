# Tugas Praktikum Pemrograman Web - Aplikasi Manajemen Tugas

Repository ini berisi proyek aplikasi manajemen tugas mahasiswa sebagai bagian dari tugas praktikum mata kuliah Pemrograman Aplikasi Web.

- **Nama:** Refi Ikhsanti
- **NIM:** 123140126
- **Program Studi:** Teknik Informatika

---

## 📝 Deskripsi Aplikasi

Aplikasi **Manajemen Tugas Mahasiswa** adalah sebuah *web application* sederhana yang dirancang untuk membantu mahasiswa melacak dan mengelola tugas-tugas akademik. 
Aplikasi ini sepenuhnya berjalan di sisi klien (*client-side*) dan menggunakan `localStorage` browser untuk menyimpan data, sehingga semua tugas tetap tersimpan meskipun halaman di-refresh atau browser ditutup.

### Fitur Utama
- **CRUD Penuh:** Pengguna dapat **Menambah** (Create), **Membaca** (Read), **Memperbarui** (Update data tugas dan status selesai/belum selesai), dan **Menghapus** (Delete) tugas.
- **Penyimpanan Lokal:** Data tugas disimpan secara persisten di `localStorage` peramban.
- **Validasi Form:** Mencegah pengiriman data yang tidak valid (misalnya, field kosong).
- **Filter & Pencarian:** Pengguna dapat dengan mudah mencari tugas berdasarkan nama atau mata kuliah dan memfilter berdasarkan status (Selesai, Belum Selesai, atau Semua).
- **Statistik Tugas:** Menampilkan jumlah tugas yang masih aktif atau belum selesai secara *real-time*.
- **Desain Responsif:** Tampilan yang baik di berbagai ukuran layar.

---

## 📸 Tampilan Aplikasi

Berikut adalah beberapa screenshot dari aplikasi yang sedang berjalan:

**1. Tampilan Utama dengan Daftar Tugas**
<img width="947" height="437" alt="image" src="https://github.com/user-attachments/assets/491aa8aa-0eb2-4428-b7f3-2301998412ed" />

**2. Tampilan Form dalam Mode Edit Tugas**
<img width="504" height="355" alt="image" src="https://github.com/user-attachments/assets/cd8f9e2a-4f5f-4f55-902d-e93ade37f82a" />

**3. Tampilan Fitur Filter dan Pencarian Aktif**
<img width="494" height="184" alt="image" src="https://github.com/user-attachments/assets/dbe8245c-40e7-47f8-bf77-0297861dd4e2" />
<img width="497" height="189" alt="image" src="https://github.com/user-attachments/assets/eff604f8-b207-4297-a4ad-1531ca676784" />

---

## 🛠️ Penjelasan Teknis

### Penggunaan `localStorage`

`localStorage` digunakan sebagai mekanisme penyimpanan data di sisi klien. Ini memungkinkan data tetap ada bahkan setelah sesi browser berakhir.

1.  **Menyimpan Data:** Setiap kali ada perubahan pada daftar tugas (menambah, mengedit, mengubah status, atau menghapus), array `tasks` yang berisi semua objek tugas akan diubah menjadi format string JSON menggunakan `JSON.stringify()`. Kemudian, data tersebut disimpan ke `localStorage` dengan *key* `'tasks'`.
    ```javascript
    const saveTasks = () => {
        localStorage.setItem('tasks', JSON.stringify(tasks));
    };
    ```

2.  **Mengambil Data:** Saat aplikasi pertama kali dimuat, skrip akan mencoba mengambil data dari `localStorage` dengan *key* `'tasks'`. Data yang diambil masih berupa string JSON, sehingga perlu diubah kembali menjadi array JavaScript menggunakan `JSON.parse()`. Jika tidak ada data yang ditemukan, sebuah array kosong `[]` akan digunakan sebagai nilai default.
    ```javascript
    let tasks = JSON.parse(localStorage.getItem('tasks')) || [];
    ```

### Fungsionalitas Edit dan Validasi Form

Logika aplikasi menangani penambahan dan pembaruan tugas melalui satu form yang sama dengan bantuan variabel state.

- **State Management Sederhana:** Sebuah variabel `editingTaskId` digunakan untuk melacak apakah pengguna sedang dalam mode edit atau tidak. Jika nilainya `null`, form berfungsi untuk menambah tugas baru. Jika berisi ID tugas, form akan berfungsi untuk memperbarui tugas tersebut.
- **Validasi Form:** Validasi diimplementasikan pada event `submit` form. Sebelum tugas baru dibuat atau tugas yang ada diperbarui, skrip akan memeriksa apakah semua input (Nama Tugas, Mata Kuliah, dan Deadline) sudah diisi. Metode `.trim()` digunakan untuk memastikan input yang hanya berisi spasi dianggap tidak valid. Jika validasi gagal, sebuah `alert()` akan muncul dan proses dibatalkan.
    ```javascript
    taskForm.addEventListener('submit', (e) => {
        e.preventDefault();
        // Validasi input...
        
        if (editingTaskId) {
            // Logika untuk UPDATE tugas yang ada
        } else {
            // Logika untuk CREATE tugas baru
        }
    });
    ```
