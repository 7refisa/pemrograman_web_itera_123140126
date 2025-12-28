Pyramid Matakuliah - REST API
==============================

Aplikasi REST API untuk mengelola data mata kuliah menggunakan Pyramid Framework.

Fitur Utama
-----------
- CRUD lengkap untuk data mata kuliah (Create, Read, Update, Delete)
- Validasi input data (kode MK, nama, SKS, semester)
- Unique constraint untuk kode mata kuliah
- Response JSON dengan pesan informatif
- Database SQLite untuk storage

Endpoint API
------------
GET    /api/matakuliah      - Mengambil semua data mata kuliah
GET    /api/matakuliah/{id} - Mengambil satu data berdasarkan ID
POST   /api/matakuliah      - Menambah mata kuliah baru
PUT    /api/matakuliah/{id} - Update data mata kuliah
DELETE /api/matakuliah/{id} - Hapus data mata kuliah

Installasi
----------
1. Pastikan virtual environment sudah aktif di root project

2. Install dependencies:
   pip install -e ".[testing]"

3. Setup database:
   alembic -c development.ini upgrade head

4. Jalankan server:
   pserve development.ini

5. Akses API:
   http://localhost:6544/api/matakuliah

Structure Data
--------------
Mata Kuliah:
- kode_mk: Kode mata kuliah (unique, required)
- nama_mk: Nama mata kuliah (required)
- sks: Jumlah SKS (integer, required)
- semester: Semester ditawarkan (integer, required)

Contoh Request
--------------
Tambah mata kuliah baru:

curl -X POST http://localhost:6544/api/matakuliah \
  -H "Content-Type: application/json" \
  -d '{
    "kode_mk": "IF301",
    "nama_mk": "Pemrograman Web",
    "sks": 3,
    "semester": 5
  }'

Testing
-------
pytest                    # Run all tests
pytest --cov             # With coverage

Development
-----------
File penting:
- models/matakuliah.py   - Model database
- views/matakuliah.py    - View handlers
- routes.py              - URL routing
- alembic/               - Database migrations

Author: Refi (123140126)

    env/bin/pserve development.ini
