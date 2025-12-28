## Deskripsi

- **Fungsi aplikasi**: Aplikasi web sederhana yang menampilkan halaman statis dan form input untuk demo penggunaan localStorage dan validasi form di sisi klien.
- **Fitur utama**: Menampilkan daftar data sederhana, menyimpan data ke `localStorage`, form input dengan validasi, dan navigasi halaman dasar.

## Screenshot

<img width="1920" height="1080" alt="Screenshot 2025-12-28 104210" src="https://github.com/user-attachments/assets/491a5faa-e2bc-42ad-807c-3ddbc0539c85" />

— Tampilan halaman utama (daftar data)

<img width="1920" height="1080" alt="Screenshot 2025-12-28 104335" src="https://github.com/user-attachments/assets/c965bef7-0bc0-4f50-bec2-46d441c5d1d0" />

— Tampilan form input dengan pesan validasi

<img width="629" height="171" alt="Screenshot 2025-12-28 104440" src="https://github.com/user-attachments/assets/a1a7e187-41ad-4b88-95f7-48e697637833" />

— Tampilan setelah menyimpan data ke localStorage

## Cara Menjalankan Aplikasi (Lokal)

1. Buka folder `refi_123140126_pertemuan1` di terminal.
2. Buka file `index.html` di browser (klik file atau gunakan server statis):

```powershell
# (opsional) Jalankan server cepat bila ingin: dari folder yang berisi index.html
python -m http.server 8000
# lalu buka http://localhost:8000/index.html
```

## Daftar Fitur yang Diimplementasikan

- Menampilkan daftar item sederhana (HTML + CSS).
- Form input untuk menambah item baru.
- Validasi input: cek input kosong, cek panjang minimal, dan tangani pesan kesalahan ke pengguna.
- Menyimpan dan mengambil data dari `localStorage` sehingga data bertahan setelah reload.

## Penjelasan Teknis: Penggunaan `localStorage` dan Validasi Form

### localStorage

- `localStorage` adalah penyimpanan di browser yang menyimpan data sebagai pasangan kunci-nilai string.
- Contoh penggunaan:
  - Menyimpan: `localStorage.setItem('books', JSON.stringify(booksArray));`
  - Mengambil: `const books = JSON.parse(localStorage.getItem('books') || '[]');`
- Dalam aplikasi ini, data yang dimasukkan lewat form diubah jadi objek, kemudian kita ambil seluruh array dari `localStorage`, push item baru, lalu simpan kembali dengan `setItem`.

### Validasi Form (Sisi Klien)

- Sebelum menyimpan, kita cek kondisi input seperti `if (!title) { showError('Judul kosong'); return; }`.
- Validasi dilakukan di event listener form `submit`.
- Bila validasi gagal, tampilkan pesan di elemen DOM (mis. `<div class="error">`), dan jangan panggil fungsi penyimpanan.
- Setelah validasi sukses, bersihkan pesan error dan lakukan proses penyimpanan.
