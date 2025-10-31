# Aplikasi Manajemen Buku Pribadi
Aplikasi web berbasis React untuk mengelola koleksi buku pribadi. Pengguna dapat melacak buku yang mereka miliki, yang sedang dibaca, atau yang ingin mereka beli di masa depan.
Aplikasi ini dibangun sebagai proyek untuk memenuhi persyaratan tugas, dengan fokus pada implementasi fitur-fitur modern React seperti Hooks, Context API, React Router, dan Custom Hooks.

## 1. Deskripsi Aplikasi & Fitur
Aplikasi ini memungkinkan pengguna untuk melakukan manajemen buku secara penuh (CRUD) dengan fitur-fitur utama:
* **Tambah, Edit, & Hapus Buku**: Pengguna dapat menambahkan buku baru dengan judul, penulis, dan status, serta mengedit atau menghapusnya.
* **Manajemen Status**: Setiap buku dapat diberi status:
    * Dimiliki (Buku yang sudah ada di rak)
    * Sedang Dibaca (Buku yang sedang aktif dibaca)
    * Akan Dibeli (Buku yang ada di *wishlist*)
* **Filter & Pencarian**: Pengguna dapat dengan mudah menemukan buku dengan:
    * Mencari berdasarkan judul atau penulis.
    * Memfilter berdasarkan status (Semua, Dimiliki, Dibaca, Akan Dibeli).
* **Penyimpanan Lokal**: Semua data buku disimpan secara persisten di `localStorage` browser, sehingga daftar buku tidak akan hilang saat browser ditutup.
* **Halaman Statistik**: Halaman terpisah (`/stats`) yang menampilkan rangkuman jumlah buku berdasarkan total dan status.
* **Navigasi Multi-Halaman**: Menggunakan React Router untuk berpindah antara halaman "Home" dan "Statistik".

## 2. Instruksi Instalasi dan Menjalankan
Untuk menjalankan proyek ini di komputer lokal Anda, ikuti langkah-langkah berikut:
**Prasyarat:**
* Node.js (v16 atau lebih baru)
* NPM (atau Yarn)

**Langkah-langkah:**
1.  **Clone repositori** (atau unduh file dan letakkan di dalam folder).
    ```bash
    git clone [URL-REPOSITORI-ANDA]
    ```
2.  **Masuk ke direktori proyek:**
    ```bash
    cd refi_123140126_pertemuan3
    ```
3.  **Install semua dependensi** yang diperlukan:
    ```bash
    npm install
    ```
4.  **Jalankan server development:**
    ```bash
    npm start
    ```
    Aplikasi akan otomatis terbuka di browser Anda pada alamat `http://localhost:3000`.
5.  **Untuk menjalankan testing:**
    ```bash
    npm test
    ```

## 3. Screenshot Antarmuka
Berikut adalah beberapa tampilan antarmuka aplikasi:
**Halaman Utama (Daftar Buku dan Filter)**
![Halaman Utama](<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/909cba12-e388-493a-a6ad-55546e2e082a" />)

**Modal Form (Tambah Buku)**
![Modal Form](<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/8bd090c6-c3f4-4e11-a266-9c577b52dffc" />)

**Halaman Statistik**
![Halaman Statistik](<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/f5941ccf-d058-4160-8ddc-a0e2e88154ea" />)


## 4. Penjelasan Fitur React yang Digunakan
Proyek ini mengimplementasikan berbagai konsep inti dan modern React:
* **`useState` & `useEffect`**:
    * `useState` digunakan secara ekstensif untuk mengelola *state* lokal di dalam komponen, seperti input pada `BookForm.js`, nilai filter pada `BookFilter.js`, dan status *modal* pada `Home.js`.
    * `useEffect` digunakan di dalam `BookContext.js` untuk memicu penyimpanan data ke `localStorage` setiap kali *state* `books` berubah.

* **Komponen Reusable**:
    * Proyek dipecah menjadi beberapa komponen modular yang dapat digunakan kembali, seperti:
        * `Navbar/Navbar.js`: Menampilkan navigasi yang konsisten.
        * `BookForm/BookForm.js`: Form yang digunakan untuk *menambah* dan *mengedit* buku.
        * `BookList/BookList.js`: Menampilkan daftar buku.
        * `BookFilter/BookFilter.js`: Menyediakan fungsionalitas pencarian dan filter.

* **Context API (`src/context/BookContext.js`)**:
    * Digunakan sebagai solusi *state management* global.
    * `BookContext` menyediakan *state* `books` dan fungsi-fungsi *dispatcher* (`addBook`, `editBook`, `deleteBook`) ke seluruh komponen di dalam aplikasi.
    * Ini menghindari *prop-drilling* (melempar props berkali-kali ke komponen anak).

* **React Router (`react-router-dom`)**:
    * Digunakan untuk membuat aplikasi menjadi *Multi-Page Application (MPA)* secara virtual.
    * Rute utama diatur di `App.js` menggunakan `<Routes>` dan `<Route>`.
    * `Navbar.js` menggunakan `<NavLink>` untuk navigasi dan penanda *link aktif* secara otomatis.

* **Custom Hooks**:
    * **`useLocalStorage.js`**: Hook kustom (`src/hooks/useLocalStorage.js`) yang dibuat untuk mengabstraksi logika `localStorage`. Hook ini secara otomatis mengambil data dari `localStorage` saat inisialisasi dan menyimpan data baru setiap kali *state* terkait (yang ada di *Context*) berubah.
    * **`useBookStats.js`**: Hook kustom (`src/hooks/useBookStats.js`) yang berisi logika untuk mengkalkulasi statistik buku. Ini memisahkan logika bisnis dari komponen tampilan (`Stats.js`) dan membuatnya lebih bersih.

* **Error Handling (Form)**:
    * Di dalam `BookForm.js`, diterapkan validasi input sederhana. Jika pengguna mencoba menyimpan tanpa mengisi judul atau penulis, *state* `errors` akan diatur dan pesan kesalahan akan ditampilkan di bawah input yang relevan.


## 5. Laporan Testing
*Testing* dilakukan menggunakan **React Testing Library** dan **Jest**. File tes utama adalah `src/App.test.js`.
<img width="426" height="169" alt="image" src="https://github.com/user-attachments/assets/2062109b-5c82-4da2-8c66-4dbc90e9896a" />

**Perintah untuk Menjalankan Tes:**
```bash
npm test
