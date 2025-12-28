## Deskripsi
Repository ini berisi 2 aplikasi REST API yang dibangun menggunakan Pyramid Framework dan SQLAlchemy ORM:

1. **pyramid_mahasiswa** - API untuk mengelola data mahasiswa
2. **pyramid_matakuliah** - API untuk mengelola data mata kuliah

Kedua aplikasi ini menyediakan endpoint RESTful lengkap untuk operasi CRUD (Create, Read, Update, Delete) dengan database SQLite.

## Struktur Project
```
refi_123140126_pertemuan6/
├── pyramid_mahasiswa/          # Aplikasi Mahasiswa
│   ├── pyramid_mahasiswa/
│   │   ├── models/            # Database models
│   │   ├── views/             # View handlers (controllers)
│   │   ├── templates/         # Jinja2 templates
│   │   ├── static/            # Static files (CSS, JS)
│   │   ├── alembic/           # Database migrations
│   │   ├── routes.py          # URL routing
│   │   └── __init__.py        # App initialization
│   ├── development.ini        # Development config
│   └── setup.py              # Package setup
│
└── pyramid_matakuliah/        # Aplikasi Matakuliah
    ├── pyramid_matakuliah/
    │   ├── models/            # Database models
    │   ├── views/             # View handlers (controllers)
    │   ├── templates/         # Jinja2 templates
    │   ├── static/            # Static files
    │   ├── alembic/           # Database migrations
    │   ├── routes.py          # URL routing
    │   └── __init__.py        # App initialization
    ├── development.ini        # Development config
    └── setup.py              # Package setup
```

## Cara Menjalankan
### Prerequisites
- Python 3.8+ sudah terinstall
- Virtual environment sudah dibuat di root folder

### Setup Awal (Hanya Sekali)
**1. Aktifkan Virtual Environment**
```powershell
cd D:\Documents\05\PAW\pemrograman_web_itera_123140126
.venv\Scripts\activate
```

**2. Install Dependencies Pyramid Mahasiswa**
```powershell
cd refi_123140126_pertemuan6\pyramid_mahasiswa
pip install -e ".[testing]"
alembic -c development.ini upgrade head
initialize_pyramid_mahasiswa_db development.ini
```

**3. Install Dependencies Pyramid Matakuliah**
```powershell
cd ..\pyramid_matakuliah
pip install -e ".[testing]"
alembic -c development.ini upgrade head
```

### Menjalankan Server (Setiap Kali)
**Opsi 1: Menggunakan 2 Terminal PowerShell (Recommended)**
```powershell
# Terminal 1 - Server Mahasiswa
cd D:\Documents\05\PAW\pemrograman_web_itera_123140126\refi_123140126_pertemuan6\pyramid_mahasiswa
D:/Documents/05/PAW/pemrograman_web_itera_123140126/.venv/Scripts/pserve.exe development.ini

# Terminal 2 - Server Matakuliah
cd D:\Documents\05\PAW\pemrograman_web_itera_123140126\refi_123140126_pertemuan6\pyramid_matakuliah
D:/Documents/05/PAW/pemrograman_web_itera_123140126/.venv/Scripts/pserve.exe development.ini
```

**Opsi 2: Menggunakan Start-Process (Background)**
```powershell
# Jalankan kedua server sekaligus
cd D:\Documents\05\PAW\pemrograman_web_itera_123140126\refi_123140126_pertemuan6\pyramid_mahasiswa
Start-Process -FilePath "D:/Documents/05/PAW/pemrograman_web_itera_123140126/.venv/Scripts/pserve.exe" -ArgumentList "development.ini" -WindowStyle Normal

cd ..\pyramid_matakuliah
Start-Process -FilePath "D:/Documents/05/PAW/pemrograman_web_itera_123140126/.venv/Scripts/pserve.exe" -ArgumentList "development.ini" -WindowStyle Normal
```

### URL Akses
- **API Mahasiswa**: http://localhost:6543/api/mahasiswa
- **API Matakuliah**: http://localhost:6544/api/matakuliah

## API Endpoints
### API Mahasiswa (Port 6543)
| Method | Endpoint              | Deskripsi                               |
| ------ | --------------------- | --------------------------------------- |
| GET    | `/api/mahasiswa`      | Mengambil semua data mahasiswa          |
| GET    | `/api/mahasiswa/{id}` | Mengambil data mahasiswa berdasarkan ID |
| POST   | `/api/mahasiswa`      | Menambah mahasiswa baru                 |
| PUT    | `/api/mahasiswa/{id}` | Mengupdate data mahasiswa               |
| DELETE | `/api/mahasiswa/{id}` | Menghapus data mahasiswa                |

#### Request Body untuk POST/PUT Mahasiswa
```json
{
  "nim": "123140126",
  "nama": "Refi",
  "jurusan": "Informatika",
  "tanggal_lahir": "2000-01-15",
  "alamat": "Bandar Lampung"
}
```

### API Matakuliah (Port 6544)
| Method | Endpoint               | Deskripsi                                 |
| ------ | ---------------------- | ----------------------------------------- |
| GET    | `/api/matakuliah`      | Mengambil semua data mata kuliah          |
| GET    | `/api/matakuliah/{id}` | Mengambil data mata kuliah berdasarkan ID |
| POST   | `/api/matakuliah`      | Menambah mata kuliah baru                 |
| PUT    | `/api/matakuliah/{id}` | Mengupdate data mata kuliah               |
| DELETE | `/api/matakuliah/{id}` | Menghapus data mata kuliah                |

#### Request Body untuk POST/PUT Matakuliah
```json
{
  "kode_mk": "IF101",
  "nama_mk": "Pemrograman Web",
  "sks": 3,
  "semester": 5
}
```

## Contoh Penggunaan API
### GET - Mengambil Semua Data Mahasiswa
**Request:**
```bash
curl http://localhost:6543/api/mahasiswa
```

**Response:**
```json
{
  "mahasiswas": [
    {
      "id": 1,
      "nim": "12345",
      "nama": "Budi Santoso",
      "jurusan": "Teknik Informatika",
      "alamat": "Jl. Merdeka No. 123, Bandung",
      "tanggal_lahir": "2000-05-15"
    },
    {
      "id": 2,
      "nim": "54321",
      "nama": "Siti Aminah",
      "jurusan": "Sistem Informasi",
      "alamat": "Jl. Mawar No. 45, Jakarta",
      "tanggal_lahir": "2001-08-22"
    }
  ]
}
```

### POST - Menambah Mahasiswa Baru
**Request:**
```bash
curl -X POST http://localhost:6543/api/mahasiswa \
  -H "Content-Type: application/json" \
  -d '{
    "nim": "123140126",
    "nama": "Refi",
    "jurusan": "Teknik Informatika",
    "tanggal_lahir": "2003-06-10",
    "alamat": "Bandar Lampung"
  }'
```

**Response:**
```json
{
  "success": true,
  "message": "Data mahasiswa berhasil ditambahkan",
  "mahasiswa": {
    "id": 3,
    "nim": "123140126",
    "nama": "Refi",
    "jurusan": "Teknik Informatika",
    "tanggal_lahir": "2003-06-10",
    "alamat": "Bandar Lampung"
  }
}
```

### PUT - Update Data Mahasiswa
**Request:**
```bash
curl -X PUT http://localhost:6543/api/mahasiswa/1 \
  -H "Content-Type: application/json" \
  -d '{"alamat": "Jl. Sudirman No. 100, Bandung"}'
```

### DELETE - Hapus Data Mahasiswa
**Request:**
```bash
curl -X DELETE http://localhost:6543/api/mahasiswa/1
```

**Response:**
```json
{
  "success": true,
  "message": "Data mahasiswa \"Budi Santoso\" (ID: 1) berhasil dihapus"
}
```

### API Matakuliah - Contoh Penggunaan
**GET All:**
```bash
curl http://localhost:6544/api/matakuliah
```

**POST New:**
```bash
curl -X POST http://localhost:6544/api/matakuliah \
  -H "Content-Type: application/json" \
  -d '{
    "kode_mk": "IF301",
    "nama_mk": "Pemrograman Web",
    "sks": 3,
    "semester": 5
  }'
```

## Database
- **pyramid_mahasiswa.db** - Database untuk aplikasi mahasiswa
- **pyramid_matakuliah.db** - Database untuk aplikasi matakuliah

### Schema Database
#### Tabel Mahasiswa
| Kolom         | Tipe    | Constraint       |
| ------------- | ------- | ---------------- |
| id            | Integer | Primary Key      |
| nim           | Text    | Unique, Not Null |
| nama          | Text    | Not Null         |
| jurusan       | Text    | Not Null         |
| tanggal_lahir | Date    | Nullable         |
| alamat        | Text    | Nullable         |

#### Tabel Matakuliah
| Kolom    | Tipe    | Constraint       |
| -------- | ------- | ---------------- |
| id       | Integer | Primary Key      |
| kode_mk  | Text    | Unique, Not Null |
| nama_mk  | Text    | Not Null         |
| sks      | Integer | Not Null         |
| semester | Integer | Not Null         |


## Fitur yang Diimplementasikan
### Pyramid Mahasiswa
- ✅ Full CRUD operations (Create, Read, Update, Delete)
- ✅ Validasi input data (field required, format tanggal)
- ✅ Unique constraint untuk NIM
- ✅ Format tanggal otomatis (ISO format)
- ✅ Response JSON yang konsisten
- ✅ Error handling dengan pesan yang jelas
- ✅ Message informatif untuk setiap operasi

### Pyramid Matakuliah
- ✅ Full CRUD operations
- ✅ Validasi input data (field required, tipe data)
- ✅ Unique constraint untuk kode mata kuliah
- ✅ Response JSON yang konsisten
- ✅ Error handling yang baik
- ✅ Message informatif untuk setiap operasi

## Development
### Struktur Code
- **models/** - Definisi model database (SQLAlchemy)
- **views/** - View functions untuk handle HTTP requests
- **routes.py** - Konfigurasi URL routing
- **alembic/** - Database migration scripts
- **templates/** - Jinja2 templates
- **static/** - CSS dan assets

### Database Migrations
```bash
# Membuat migration baru
alembic -c development.ini revision --autogenerate -m "description"

# Apply migration
alembic -c development.ini upgrade head

# Rollback migration
alembic -c development.ini downgrade -1
```