Pyramid Mahasiswa - REST API
============================

Aplikasi REST API untuk mengelola data mahasiswa menggunakan Pyramid Framework.

Fitur Utama
-----------
- CRUD lengkap untuk data mahasiswa (Create, Read, Update, Delete)
- Validasi input data dan format tanggal
- Unique constraint untuk NIM
- Response JSON dengan pesan informatif
- Database SQLite untuk storage

Endpoint API
------------
GET    /api/mahasiswa      - Mengambil semua data mahasiswa
GET    /api/mahasiswa/{id} - Mengambil satu data berdasarkan ID
POST   /api/mahasiswa      - Menambah mahasiswa baru
PUT    /api/mahasiswa/{id} - Update data mahasiswa
DELETE /api/mahasiswa/{id} - Hapus data mahasiswa

Installasi
----------
1. Pastikan virtual environment sudah aktif di root project

2. Install dependencies:
   pip install -e ".[testing]"

3. Setup database:
   alembic -c development.ini upgrade head
   initialize_pyramid_mahasiswa_db development.ini

4. Jalankan server:
   pserve development.ini

5. Akses API:
   http://localhost:6543/api/mahasiswa

Data Awal
---------
Database sudah berisi 2 data mahasiswa:
1. Budi Santoso (NIM: 12345) - Teknik Informatika
2. Siti Aminah (NIM: 54321) - Sistem Informasi

Contoh Request
--------------
Tambah mahasiswa baru:

curl -X POST http://localhost:6543/api/mahasiswa \
  -H "Content-Type: application/json" \
  -d '{
    "nim": "123140126",
    "nama": "Refi",
    "jurusan": "Teknik Informatika",
    "tanggal_lahir": "2003-06-10",
    "alamat": "Bandar Lampung"
  }'

Testing
-------
pytest                    # Run all tests
pytest --cov             # With coverage

Development
-----------
File penting:
- models/mahasiswa.py    - Model database
- views/mahasiswa.py     - View handlers
- routes.py              - URL routing
- alembic/               - Database migrations

Author: Refi (123140126)

    env/bin/pserve development.ini
