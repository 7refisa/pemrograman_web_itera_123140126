# Aplikasi Personal Dashboard - Jadwal Kuliah
Aplikasi web sederhana untuk mengelola jadwal kuliah pribadi. Aplikasi ini memungkinkan pengguna untuk menambah, mengedit, dan menghapus item jadwal. Semua data disimpan secara lokal di browser pengguna menggunakan `localStorage`.

## Fungsi dan Fitur
Aplikasi ini memiliki beberapa fungsionalitas utama untuk mengelola jadwal:

  * **Tambah Jadwal:** Pengguna dapat menambahkan jadwal kuliah baru melalui formulir di bagian atas, menentukan Hari, Mata Kuliah, Lokasi, dan Waktu.
  * **Edit Jadwal:** Dengan mengklik tombol "Edit" pada kartu jadwal, data akan dimuat kembali ke formulir. Pengguna dapat memperbarui informasi dan menyimpannya dengan tombol "Update Jadwal".
  * **Hapus Jadwal:** Tombol "Hapus" pada setiap kartu akan memunculkan dialog konfirmasi untuk menghapus item jadwal secara permanen dari `localStorage`.
  * **Penyimpanan Lokal:** Semua data jadwal disimpan di `localStorage` browser. Ini memastikan bahwa jadwal tetap ada bahkan setelah menutup tab atau browser dan membukanya kembali.
  * **Tampilan Papan (Board View):** Jadwal diatur dengan rapi ke dalam kolom berdasarkan hari (Senin-Jumat) untuk visualisasi yang mudah.

## Screenshot Aplikasi
Berikut adalah beberapa tangkapan layar dari aplikasi yang sedang digunakan:

**Tampilan Utama Aplikasi**
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/9f1accb8-6daa-4d72-8ec9-ddde948d13b0" />

**Proses Menambah Data**
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/0033d103-52ff-47cf-9e76-debc5fcf2021" />

**Proses Edit Data**
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/7f174489-853d-4eb2-9cbd-fe9a1f244826" />

**Konfirmasi Hapus Data**
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/939a0a48-cf9f-448e-b860-085a8ae91f0d" />

## Daftar Fitur ES6+ yang Diimplementasikan
Sesuai dengan persyaratan tugas, proyek ini mengimplementasikan fitur-fitur ES6+ berikut:

1.  **`let` dan `const`:**

      * **`const`** digunakan untuk variabel yang tidak akan di-reassign, seperti elemen DOM (`this.form`, `this.boardContainer`) dan variabel di dalam *scope* fungsi (`cardHTML`, `day`, `courseName`).
      * **`let`** digunakan untuk variabel yang nilainya bisa berubah, seperti `this.items` yang menyimpan *state* aplikasi.

2.  **Arrow Functions (Fungsi Panah):**

      * Digunakan secara ekstensif untuk *event listener* (pada `submit` form, `click` tombol batal, dan *event delegation* pada `boardContainer`) untuk mempertahankan *scope* `this` agar tetap merujuk ke *instance* `ScheduleApp`.
      * Contoh: `this.form.addEventListener('submit', (e) => { ... })` dan `this.cancelButton.addEventListener('click', () => { ... })`.

3.  **Template Literals:**

      * Digunakan dalam metode `renderItems()` untuk membuat blok HTML kartu jadwal secara dinamis. Ini memungkinkan penyisipan variabel (seperti `${item.id}` dan `${item.courseName}`) langsung ke dalam string dengan cara yang bersih.

4.  **Classes:**

      * **`class ScheduleItem`**: Digunakan sebagai *blueprint* (model data) untuk setiap objek jadwal, mengelola properti seperti `id`, `day`, `courseName`, dll.
      * **`class ScheduleApp`**: Kelas utama yang membungkus semua logika aplikasi, termasuk *state* (`this.items`), metode (`init`, `addItem`, `deleteItem`, `renderItems`, dll.), dan *event listener*.

5.  **Fungsi Asinkron (Async/Await dan Promises):**

      * **Promises**: Metode `fetchDataFromStorage()` mengembalikan `new Promise` yang di-*resolve* setelah `setTimeout`, mensimulasikan operasi I/O asinkron (seperti panggilan API).
      * **Async/Await**: Metode `init()` dideklarasikan sebagai `async` dan menggunakan `await` untuk menunggu `fetchDataFromStorage()` selesai sebelum mencoba me-render data ke layar, memastikan tidak ada *race condition* saat memuat.
