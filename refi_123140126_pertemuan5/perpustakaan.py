from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Optional

# Abstract Base Class untuk semua item perpustakaan
class LibraryItem(ABC):
    def __init__(self, item_id: str, title: str, year: int):
        self.__item_id = item_id  # Private
        self._title = title  # Protected
        self._year = year
        self._is_available = True
        self._borrowed_by = None
        self._borrow_date = None
    
    # Property read-only untuk item_id
    @property
    def item_id(self) -> str:
        return self.__item_id
    
    @property
    def title(self) -> str:
        return self._title
    
    @title.setter
    def title(self, value: str):
        if not value or not isinstance(value, str):
            raise ValueError("Title harus berupa string yang tidak kosong")
        self._title = value
    
    @property
    def year(self) -> int:
        return self._year
    
    @year.setter
    def year(self, value: int):
        current_year = datetime.now().year
        if not isinstance(value, int) or value < 1000 or value > current_year:
            raise ValueError(f"Year harus antara 1000 dan {current_year}")
        self._year = value
    
    @property
    def is_available(self) -> bool:
        return self._is_available
    
    # Abstract method - harus diimplementasikan subclass
    @abstractmethod
    def get_item_type(self) -> str:
        pass
    
    # Abstract method - harus diimplementasikan subclass
    @abstractmethod
    def get_description(self) -> str:
        pass
    
    # Method untuk meminjam item
    def borrow(self, borrower_name: str) -> bool:
        if not self._is_available:
            return False
        
        self._is_available = False
        self._borrowed_by = borrower_name
        self._borrow_date = datetime.now()
        return True
    
    # Method untuk mengembalikan item
    def return_item(self) -> bool:
        if self._is_available:
            return False
        
        self._is_available = True
        self._borrowed_by = None
        self._borrow_date = None
        return True
    
    # Mendapatkan informasi peminjaman
    def get_borrow_info(self) -> dict:
        return {
            'borrowed_by': self._borrowed_by,
            'borrow_date': self._borrow_date.strftime('%Y-%m-%d %H:%M:%S') if self._borrow_date else None,
            'is_available': self._is_available
        }
    
    def __str__(self) -> str:
        status = "Tersedia" if self._is_available else f"Dipinjam oleh {self._borrowed_by}"
        return f"[{self.item_id}] {self.title} ({self.year}) - {status}"

# Class Book - inheritance dari LibraryItem
class Book(LibraryItem):
    def __init__(self, item_id: str, title: str, year: int, author: str, pages: int, isbn: str):
        super().__init__(item_id, title, year)
        self.__author = author  # Private
        self.__pages = pages
        self.__isbn = isbn
    
    @property
    def author(self) -> str:
        return self.__author
    
    @author.setter
    def author(self, value: str):
        if not value or not isinstance(value, str):
            raise ValueError("Author harus berupa string yang tidak kosong")
        self.__author = value
    
    @property
    def pages(self) -> int:
        return self.__pages
    
    @property
    def isbn(self) -> str:
        return self.__isbn
    
    # Implementation abstract method
    def get_item_type(self) -> str:
        return "Buku"
    
    # Implementation abstract method
    def get_description(self) -> str:
        return (f"Tipe: {self.get_item_type()}\n"
                f"ID: {self.item_id}\n"
                f"Judul: {self.title}\n"
                f"Penulis: {self.__author}\n"
                f"Tahun: {self.year}\n"
                f"Halaman: {self.__pages}\n"
                f"ISBN: {self.__isbn}\n"
                f"Status: {'Tersedia' if self.is_available else f'Dipinjam oleh {self._borrowed_by}'}")
    
    # Polymorphism - override __str__
    def __str__(self) -> str:
        status = "Tersedia" if self.is_available else f"Dipinjam"
        return f"📚 [{self.item_id}] {self.title} - {self.__author} ({self.year}) | {self.__pages} hal. | {status}"

# Class Magazine - inheritance dari LibraryItem
class Magazine(LibraryItem):
    def __init__(self, item_id: str, title: str, year: int, publisher: str, edition: str, issue_number: int):
        super().__init__(item_id, title, year)
        self.__publisher = publisher  # Private
        self.__edition = edition
        self.__issue_number = issue_number
    
    @property
    def publisher(self) -> str:
        return self.__publisher
    
    @publisher.setter
    def publisher(self, value: str):
        if not value or not isinstance(value, str):
            raise ValueError("Publisher harus berupa string yang tidak kosong")
        self.__publisher = value
    
    @property
    def edition(self) -> str:
        return self.__edition
    
    @property
    def issue_number(self) -> int:
        return self.__issue_number
    
    # Implementation abstract method
    def get_item_type(self) -> str:
        return "Majalah"
    
    # Implementation abstract method
    def get_description(self) -> str:
        return (f"Tipe: {self.get_item_type()}\n"
                f"ID: {self.item_id}\n"
                f"Judul: {self.title}\n"
                f"Penerbit: {self.__publisher}\n"
                f"Edisi: {self.__edition}\n"
                f"Nomor Edisi: {self.__issue_number}\n"
                f"Tahun: {self.year}\n"
                f"Status: {'Tersedia' if self.is_available else f'Dipinjam oleh {self._borrowed_by}'}")
    
    # Polymorphism - override __str__
    def __str__(self) -> str:
        status = "Tersedia" if self.is_available else f"Dipinjam"
        return f"📰 [{self.item_id}] {self.title} - Ed. {self.__edition} (No. {self.__issue_number}) | {status}"

# Class Newspaper - inheritance dari LibraryItem
class Newspaper(LibraryItem):
    def __init__(self, item_id: str, title: str, year: int, publisher: str, date: str):
        super().__init__(item_id, title, year)
        self.__publisher = publisher  # Private
        self.__date = date
    
    @property
    def publisher(self) -> str:
        return self.__publisher
    
    @property
    def date(self) -> str:
        return self.__date
    
    # Implementation abstract method
    def get_item_type(self) -> str:
        return "Koran"
    
    # Implementation abstract method
    def get_description(self) -> str:
        return (f"Tipe: {self.get_item_type()}\n"
                f"ID: {self.item_id}\n"
                f"Judul: {self.title}\n"
                f"Penerbit: {self.__publisher}\n"
                f"Tanggal: {self.__date}\n"
                f"Tahun: {self.year}\n"
                f"Status: {'Tersedia' if self.is_available else f'Dipinjam oleh {self._borrowed_by}'}")
    
    # Polymorphism - override __str__
    def __str__(self) -> str:
        status = "Tersedia" if self.is_available else f"Dipinjam"
        return f"📰 [{self.item_id}] {self.title} - {self.__date} | {status}"

# Class Library untuk mengelola koleksi perpustakaan
class Library:
    def __init__(self, name: str):
        self.__name = name  # Private
        self.__items: List[LibraryItem] = []  # Private
        self.__total_borrowed = 0  # Private
    
    @property
    def name(self) -> str:
        return self.__name
    
    # Property read-only untuk total items
    @property
    def total_items(self) -> int:
        return len(self.__items)
    
    # Property read-only untuk available items
    @property
    def available_items(self) -> int:
        return sum(1 for item in self.__items if item.is_available)
    
    # Property read-only untuk borrowed items
    @property
    def borrowed_items(self) -> int:
        return self.total_items - self.available_items
    
    # Menambahkan item ke perpustakaan
    def add_item(self, item: LibraryItem) -> bool:
        if any(existing_item.item_id == item.item_id for existing_item in self.__items):
            return False
        self.__items.append(item)
        return True
    
    # Menghapus item dari perpustakaan
    def remove_item(self, item_id: str) -> bool:
        for i, item in enumerate(self.__items):
            if item.item_id == item_id:
                self.__items.pop(i)
                return True
        return False
    
    # Mencari item berdasarkan ID
    def find_by_id(self, item_id: str) -> Optional[LibraryItem]:
        for item in self.__items:
            if item.item_id == item_id:
                return item
        return None
    
    # Mencari item berdasarkan judul (partial match, case-insensitive)
    def find_by_title(self, title: str) -> List[LibraryItem]:
        title_lower = title.lower()
        return [item for item in self.__items if title_lower in item.title.lower()]
    
    # Mendapatkan items berdasarkan tipe
    def get_items_by_type(self, item_type: str) -> List[LibraryItem]:
        return [item for item in self.__items if item.get_item_type() == item_type]
    
    # Mendapatkan items yang tersedia
    def get_available_items(self) -> List[LibraryItem]:
        return [item for item in self.__items if item.is_available]
    
    # Mendapatkan items yang sedang dipinjam
    def get_borrowed_items(self) -> List[LibraryItem]:
        return [item for item in self.__items if not item.is_available]
    
    # Menampilkan semua item (demonstrasi polymorphism)
    def display_all_items(self) -> None:
        if not self.__items:
            print("Perpustakaan masih kosong.")
            return
        
        print(f"\n{'='*80}")
        print(f"DAFTAR KOLEKSI {self.__name.upper()}")
        print(f"{'='*80}")
        print(f"Total Item: {self.total_items} | Tersedia: {self.available_items} | Dipinjam: {self.borrowed_items}")
        print(f"{'='*80}\n")
        
        for idx, item in enumerate(self.__items, 1):
            print(f"{idx}. {item}")
    
    # Menampilkan items yang tersedia
    def display_available_items(self) -> None:
        available = self.get_available_items()
        
        if not available:
            print("Tidak ada item yang tersedia saat ini.")
            return
        
        print(f"\n{'='*80}")
        print(f"ITEM TERSEDIA DI {self.__name.upper()}")
        print(f"{'='*80}")
        print(f"Total: {len(available)} item\n")
        
        for idx, item in enumerate(available, 1):
            print(f"{idx}. {item}")
    
    # Meminjam item
    def borrow_item(self, item_id: str, borrower_name: str) -> bool:
        item = self.find_by_id(item_id)
        
        if item is None:
            return False
        
        if item.borrow(borrower_name):
            self.__total_borrowed += 1
            return True
        
        return False
    
    # Mengembalikan item
    def return_item(self, item_id: str) -> bool:
        item = self.find_by_id(item_id)
        
        if item is None:
            return False
        
        return item.return_item()
    
    # Mendapatkan statistik perpustakaan
    def get_statistics(self) -> dict:
        books = len(self.get_items_by_type("Buku"))
        magazines = len(self.get_items_by_type("Majalah"))
        newspapers = len(self.get_items_by_type("Koran"))
        
        return {
            'total_items': self.total_items,
            'available_items': self.available_items,
            'borrowed_items': self.borrowed_items,
            'total_borrowed_ever': self.__total_borrowed,
            'books': books,
            'magazines': magazines,
            'newspapers': newspapers
        }
    
    # Menampilkan statistik perpustakaan
    def display_statistics(self) -> None:
        stats = self.get_statistics()
        
        print(f"\n{'='*80}")
        print(f"STATISTIK {self.__name.upper()}")
        print(f"{'='*80}")
        print(f"Total Koleksi        : {stats['total_items']} item")
        print(f"  - Buku             : {stats['books']} item")
        print(f"  - Majalah          : {stats['magazines']} item")
        print(f"  - Koran            : {stats['newspapers']} item")
        print(f"\nStatus Peminjaman:")
        print(f"  - Tersedia         : {stats['available_items']} item")
        print(f"  - Sedang Dipinjam  : {stats['borrowed_items']} item")
        print(f"  - Total Peminjaman : {stats['total_borrowed_ever']} kali")
        print(f"{'='*80}")
    
    def __str__(self) -> str:
        return f"Perpustakaan {self.__name} - {self.total_items} items ({self.available_items} tersedia)"

if __name__ == "__main__":
    print("Testing Sistem Manajemen Perpustakaan")
    print("="*50)
    
    lib = Library("Perpustakaan ITERA")
    
    book1 = Book("BK001", "Pemrograman Python", 2023, "John Doe", 350, "978-1234567890")
    book2 = Book("BK002", "Machine Learning Basics", 2024, "Jane Smith", 420, "978-0987654321")
    magazine1 = Magazine("MG001", "Tech Monthly", 2024, "Tech Publisher", "November 2024", 145)
    newspaper1 = Newspaper("NP001", "Daily News", 2024, "News Corp", "2024-11-10")
    
    lib.add_item(book1)
    lib.add_item(book2)
    lib.add_item(magazine1)
    lib.add_item(newspaper1)
    
    lib.display_all_items()
    lib.display_statistics()
    
    print("\nTesting berhasil!")