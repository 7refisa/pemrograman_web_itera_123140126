# Sistem Manajemen Perpustakaan Sederhana

## Deskripsi Program
Sistem Manajemen Perpustakaan adalah aplikasi berbasis Python yang mengimplementasikan konsep Object-Oriented Programming (OOP) untuk mengelola koleksi perpustakaan. Program ini dirancang untuk mempermudah pengelolaan item perpustakaan seperti buku, majalah, dan koran dengan fitur peminjaman dan pengembalian.

## Fitur Program
### Fitur Utama:
1. **Manajemen Item Perpustakaan**
   - Menambah item baru (Buku, Majalah, Koran)
   - Menghapus item dari koleksi
   - Menampilkan semua item
   - Menampilkan item berdasarkan tipe

2. **Pencarian Item**
   - Pencarian berdasarkan ID item
   - Pencarian berdasarkan judul (partial match, case-insensitive)

3. **Sistem Peminjaman**
   - Meminjam item yang tersedia
   - Mengembalikan item yang dipinjam
   - Tracking peminjam dan tanggal peminjaman
   - Menampilkan item yang sedang dipinjam

4. **Statistik Perpustakaan**
   - Total koleksi per kategori
   - Jumlah item tersedia dan dipinjam
   - Total peminjaman yang pernah terjadi

## Konsep OOP yang Diimplementasikan
### 1. Abstract Class dan Inheritance
```python
# Abstract Base Class
class LibraryItem(ABC):
    @abstractmethod
    def get_item_type(self) -> str:
        pass

    @abstractmethod
    def get_description(self) -> str:
        pass

# Inheritance - Subclass
class Book(LibraryItem):
    def get_item_type(self) -> str:
        return "Buku"

    def get_description(self) -> str:
        # Implementation specific untuk Book
        ...

class Magazine(LibraryItem):
    # Implementation specific untuk Magazine
    ...

class Newspaper(LibraryItem):
    # Implementation specific untuk Newspaper
    ...
```

**Penjelasan:**
- `LibraryItem` adalah abstract base class yang mendefinisikan kontrak untuk semua item perpustakaan
- Setiap subclass (`Book`, `Magazine`, `Newspaper`) **wajib** mengimplementasikan method abstract
- Menerapkan konsep inheritance hierarchy yang jelas dan terstruktur

### 2. Encapsulation
```python
class LibraryItem(ABC):
    def __init__(self, item_id: str, title: str, year: int):
        self.__item_id = item_id      # Private attribute
        self._title = title            # Protected attribute
        self._is_available = True
        self._borrowed_by = None

class Book(LibraryItem):
    def __init__(self, item_id: str, title: str, year: int,
                 author: str, pages: int, isbn: str):
        super().__init__(item_id, title, year)
        self.__author = author         # Private attribute
        self.__pages = pages
        self.__isbn = isbn

class Library:
    def __init__(self, name: str):
        self.__name = name             # Private attribute
        self.__items = []              # Private list
        self.__total_borrowed = 0      # Private counter
```

**Penjelasan:**
- **Private attributes** (`__attribute`): Tidak bisa diakses dari luar class
- **Protected attributes** (`_attribute`): Bisa diakses oleh subclass
- Akses data hanya melalui method yang disediakan (getter/setter)
- Data sensitif dilindungi dari akses langsung

### 3. Property Decorator
```python
class LibraryItem(ABC):
    @property
    def item_id(self) -> str:
        """Read-only property"""
        return self.__item_id

    @property
    def title(self) -> str:
        """Getter untuk title"""
        return self._title

    @title.setter
    def title(self, value: str):
        """Setter dengan validasi"""
        if not value or not isinstance(value, str):
            raise ValueError("Title harus string yang tidak kosong")
        self._title = value

    @property
    def is_available(self) -> bool:
        """Read-only property untuk status"""
        return self._is_available

class Library:
    @property
    def total_items(self) -> int:
        """Computed property"""
        return len(self.__items)

    @property
    def available_items(self) -> int:
        """Computed property"""
        return sum(1 for item in self.__items if item.is_available)
```

**Penjelasan:**
- Property decorator membuat attribute yang bisa diakses seperti variable biasa
- Memungkinkan validasi data saat setter dipanggil
- Read-only property untuk data yang tidak boleh diubah
- Computed property untuk nilai yang dihitung secara dinamis

### 4. Polymorphism
```python
# Method Overriding
class LibraryItem(ABC):
    def __str__(self) -> str:
        status = "Tersedia" if self._is_available else f"Dipinjam oleh {self._borrowed_by}"
        return f"[{self.item_id}] {self.title} ({self.year}) - {status}"

class Book(LibraryItem):
    def __str__(self) -> str:
        """Override dengan implementasi khusus untuk Book"""
        status = "Tersedia" if self.is_available else f"Dipinjam"
        return f"📚 [{self.item_id}] {self.title} - {self.__author} ({self.year}) | {self.__pages} hal. | {status}"

class Magazine(LibraryItem):
    def __str__(self) -> str:
        """Override dengan implementasi khusus untuk Magazine"""
        status = "Tersedia" if self.is_available else f"Dipinjam"
        return f"📰 [{self.item_id}] {self.title} - Ed. {self.__edition} (No. {self.__issue_number}) | {status}"

# Penggunaan Polymorphism
def display_all_items(self):
    for item in self.__items:
        print(item)  # Memanggil __str__ yang sesuai dengan tipe object
```

**Penjelasan:**
- Setiap subclass memiliki implementasi `__str__()` yang berbeda
- Method yang sama (`__str__`) menghasilkan output berbeda tergantung tipe object
- Memungkinkan kode yang lebih fleksibel dan mudah di-extend

## Struktur Class (Class Diagram)
```
                   ┌────────────────────┐
                   │  <<abstract>>      │
                   │  LibraryItem       │
                   ├────────────────────┤
                   │ - __item_id        │
                   │ - _title           │
                   │ - _year            │
                   │ - _is_available    │
                   │ - _borrowed_by     │
                   ├────────────────────┤
                   │ + borrow()         │
                   │ + return_item()    │
                   │ + get_item_type()  │
                   │ + get_description()│
                   └─────────┬──────────┘
                             │
            ┌────────────────┼────────────────┐
            │                │                │
    ┌───────▼───────┐ ┌──────▼───────┐ ┌──────▼───────┐
    │     Book      │ │  Magazine    │ │  Newspaper   │
    ├───────────────┤ ├──────────────┤ ├──────────────┤
    │ - __author    │ │ - __publisher│ │ - __publisher│
    │ - __pages     │ │ - __edition  │ │ - __date     │
    │ - __isbn      │ │ - __issue_no │ │              │
    ├───────────────┤ ├──────────────┤ ├──────────────┤
    │ + get_item_   │ │ + get_item_  │ │ + get_item_  │
    │   type()      │ │   type()     │ │   type()     │
    │ + get_descrip-│ │ + get_descri │ │ + get_descri │
    │   tion()      │ │   ption()    │ │   ption()    │
    └───────────────┘ └──────────────┘ └──────────────┘

                    ┌───────────────────┐
                    │    Library        │
                    ├───────────────────┤
                    │ - __name          │
                    │ - __items[]       │
                    │ - __total_borrowed│
                    ├───────────────────┤
                    │ + add_item()      │
                    │ + remove_item()   │
                    │ + find_by_id()    │
                    │ + find_by_title() │
                    │ + borrow_item()   │
                    │ + return_item()   │
                    │ + display_all()   │
                    └───────────────────┘
```

## Struktur File
```
refi_123140126_pertemuan5/
│
├── perpustakaan.py      # File utama: class-class sistem perpustakaan
├── main.py              # Program interaktif dengan menu
├── test_oop.py          # Testing & demonstrasi konsep OOP
├── README.md            # Dokumentasi lengkap (file ini)
└── .gitignore           # Git ignore file
```

### Penjelasan File:
- **perpustakaan.py**: Core system dengan 4 class (LibraryItem, Book, Magazine, Newspaper, Library)
- **main.py**: Program interaktif dengan 11 menu untuk user
- **test_oop.py**: Automated testing untuk demonstrasi OOP concepts
- **README.md**: Dokumentasi lengkap project
- **.gitignore**: Mencegah file cache masuk ke repository

## Cara Menjalankan Program
### Prerequisites
- Python 3.7 atau lebih baru
- Tidak memerlukan library eksternal (hanya menggunakan standard library)

### Langkah-langkah:
1. **Pastikan berada di direktori yang benar:**
   ```bash
   cd refi_123140126_pertemuan5
   ```

2. **Jalankan program utama:**
   ```bash
   python main.py
   ```

3. **Atau jalankan testing di perpustakaan.py:**
   ```bash
   python perpustakaan.py
   ```

## Panduan Penggunaan
### Menu Utama
Setelah menjalankan program, akan terlihat menu dengan 12 pilihan:
![Menu Utama](image.png)

### Contoh Penggunaan:
#### 1. Menambah Item Baru
- Pilih menu **1**
- Pilih tipe item (Buku/Majalah/Koran)
- Masukkan informasi yang diminta
- Item akan ditambahkan ke perpustakaan

#### 2. Mencari Item
- **Berdasarkan ID**: Pilih menu **5**, masukkan ID lengkap (contoh: BK001)
- **Berdasarkan Judul**: Pilih menu **6**, masukkan kata kunci (partial match)

#### 3. Meminjam Item
- Pilih menu **7**
- Program akan menampilkan item yang tersedia
- Masukkan ID item yang akan dipinjam
- Masukkan nama peminjam

#### 4. Mengembalikan Item
- Pilih menu **8**
- Program akan menampilkan item yang sedang dipinjam
- Masukkan ID item yang akan dikembalikan

## Screenshot Hasil Running Program
### 1. Menu Utama
![Menu Utama](image-5.png)
_Tampilan menu utama sistem perpustakaan_

### 2. Tampilan Semua Item
![Semua Item](image-1.png)
_Daftar lengkap koleksi perpustakaan dengan polymorphism_

### 3. Statistik Perpustakaan
![Statistik](image-2.png)
_Statistik lengkap perpustakaan_

### 4. Pencarian Item
![Pencarian](image-3.png)
_Hasil pencarian berdasarkan judul_

### 5. Peminjaman Item
![Peminjaman](image-4.png)
_Proses peminjaman item_

## Fitur Teknis
### Validasi Input
- Validasi tipe data (string, integer, dll)
- Validasi range nilai (contoh: tahun tidak boleh melebihi tahun sekarang)
- Validasi ID unik (tidak boleh duplikat)

### Error Handling
- Try-except untuk menangani input yang salah
- Pesan error yang informatif
- Graceful degradation (program tidak crash)

### Data Management
- Tracking status peminjaman dengan timestamp
- Computed properties untuk statistik real-time
- Type hints untuk dokumentasi kode yang lebih baik

## Penjelasan Kode Penting
### Abstract Method
```python
@abstractmethod
def get_item_type(self) -> str:
    """Method ini WAJIB diimplementasikan oleh subclass"""
    pass
```
Method ini memaksa setiap subclass untuk memberikan implementasi sendiri.

### Property dengan Validasi
```python
@title.setter
def title(self, value: str):
    if not value or not isinstance(value, str):
        raise ValueError("Title harus string yang tidak kosong")
    self._title = value
```
Setiap kali title diubah, validasi akan dijalankan otomatis.

### Polymorphic Behavior
```python
for item in library.__items:
    print(item)  # Akan memanggil __str__ yang sesuai
```
Meski loop yang sama, output berbeda tergantung tipe object (Book/Magazine/Newspaper).