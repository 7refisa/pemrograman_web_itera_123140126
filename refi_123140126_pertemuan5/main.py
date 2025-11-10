from perpustakaan import Library, Book, Magazine, Newspaper
import os

# Membersihkan layar terminal
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Mencetak header menu
def print_header(title):
    print("\n" + "="*80)
    print(f"{title.center(80)}")
    print("="*80 + "\n")

# Menampilkan menu utama
def print_menu():
    print_header("SISTEM MANAJEMEN PERPUSTAKAAN ITERA")
    print("1.  Tambah Item Baru")
    print("2.  Tampilkan Semua Item")
    print("3.  Tampilkan Item Tersedia")
    print("4.  Tampilkan Item yang Dipinjam")
    print("5.  Cari Item berdasarkan ID")
    print("6.  Cari Item berdasarkan Judul")
    print("7.  Pinjam Item")
    print("8.  Kembalikan Item")
    print("9.  Hapus Item")
    print("10. Lihat Statistik Perpustakaan")
    print("11. Lihat Item berdasarkan Tipe")
    print("0.  Keluar")
    print("="*80)

# Menu untuk menambahkan item baru
def add_item_menu(library):
    # Menu untuk menambahkan item baru
    print_header("TAMBAH ITEM BARU")
    print("Pilih tipe item:")
    print("1. Buku")
    print("2. Majalah")
    print("3. Koran")
    print("0. Kembali")
    choice = input("\nPilihan: ").strip()
    if choice == "0":
        return
    
    try:
        item_id = input("\nMasukkan ID item: ").strip()
        title = input("Masukkan judul: ").strip()
        year = int(input("Masukkan tahun: ").strip())

        if choice == "1":
            author = input("Masukkan nama penulis: ").strip()
            pages = int(input("Masukkan jumlah halaman: ").strip())
            isbn = input("Masukkan ISBN: ").strip()
            item = Book(item_id, title, year, author, pages, isbn)

        elif choice == "2":
            publisher = input("Masukkan nama penerbit: ").strip()
            edition = input("Masukkan edisi (contoh: November 2024): ").strip()
            issue_number = int(input("Masukkan nomor edisi: ").strip())
            item = Magazine(item_id, title, year, publisher, edition, issue_number)

        elif choice == "3":
            publisher = input("Masukkan nama penerbit: ").strip()
            date = input("Masukkan tanggal (YYYY-MM-DD): ").strip()
            item = Newspaper(item_id, title, year, publisher, date)

        else:
            print("\n❌ Pilihan tidak valid!")
            input("\nTekan Enter untuk melanjutkan...")
            return
        
        if library.add_item(item):
            print(f"\n✅ Item berhasil ditambahkan!")
            print(f"\n{item.get_description()}")

        else:
            print(f"\n❌ Gagal menambahkan item. ID '{item_id}' sudah ada!")
            
    except ValueError as e:
        print(f"\n❌ Error: {e}")
    except Exception as e:
        print(f"\n❌ Terjadi kesalahan: {e}")

    input("\nTekan Enter untuk melanjutkan...")

def search_by_id_menu(library):
    # Menu untuk mencari item berdasarkan ID
    print_header("CARI ITEM BERDASARKAN ID")
    item_id = input("Masukkan ID item: ").strip()
    item = library.find_by_id(item_id)

    if item:
        print("\n✅ Item ditemukan:")
        print("-"*80)
        print(item.get_description())
        print("-"*80)
        
        # Tampilkan informasi peminjaman jika ada
        borrow_info = item.get_borrow_info()
        if not borrow_info['is_available']:
            print(f"\n📌 Dipinjam oleh: {borrow_info['borrowed_by']}")
            print(f"📅 Tanggal pinjam: {borrow_info['borrow_date']}")
    else:
        print(f"\n❌ Item dengan ID '{item_id}' tidak ditemukan!")
    
    input("\nTekan Enter untuk melanjutkan...")

def search_by_title_menu(library):
    # Menu untuk mencari item berdasarkan judul
    print_header("CARI ITEM BERDASARKAN JUDUL")
    title = input("Masukkan judul (atau sebagian judul): ").strip()
    
    items = library.find_by_title(title)
    
    if items:
        print(f"\n✅ Ditemukan {len(items)} item:")
        print("-"*80)
        for idx, item in enumerate(items, 1):
            print(f"{idx}. {item}")
        print("-"*80)
    else:
        print(f"\n❌ Tidak ada item dengan judul yang mengandung '{title}'!")
    
    input("\nTekan Enter untuk melanjutkan...")

def borrow_item_menu(library):
    # Menu untuk meminjam item
    print_header("PINJAM ITEM")
    
    # Tampilkan item yang tersedia
    available = library.get_available_items()
    
    if not available:
        print("❌ Tidak ada item yang tersedia untuk dipinjam saat ini.")
        input("\nTekan Enter untuk melanjutkan...")
        return
    
    print("Item yang tersedia:\n")
    for idx, item in enumerate(available, 1):
        print(f"{idx}. {item}")
    
    print("\n" + "-"*80)
    item_id = input("\nMasukkan ID item yang akan dipinjam: ").strip()
    borrower_name = input("Masukkan nama peminjam: ").strip()
    
    if not borrower_name:
        print("\n❌ Nama peminjam tidak boleh kosong!")
        input("\nTekan Enter untuk melanjutkan...")
        return
    
    if library.borrow_item(item_id, borrower_name):
        item = library.find_by_id(item_id)
        print(f"\n✅ Berhasil meminjam item:")
        print(f"   {item}")
        print(f"   Peminjam: {borrower_name}")
    else:
        print(f"\n❌ Gagal meminjam item. Item tidak tersedia atau tidak ditemukan!")
    
    input("\nTekan Enter untuk melanjutkan...")

def return_item_menu(library):
    # Menu untuk mengembalikan item
    print_header("KEMBALIKAN ITEM")
    
    # Tampilkan item yang sedang dipinjam
    borrowed = library.get_borrowed_items()
    
    if not borrowed:
        print("❌ Tidak ada item yang sedang dipinjam saat ini.")
        input("\nTekan Enter untuk melanjutkan...")
        return
    
    print("Item yang sedang dipinjam:\n")
    for idx, item in enumerate(borrowed, 1):
        borrow_info = item.get_borrow_info()
        print(f"{idx}. {item}")
        print(f"   Dipinjam oleh: {borrow_info['borrowed_by']} | Tanggal: {borrow_info['borrow_date']}")
    
    print("\n" + "-"*80)
    item_id = input("\nMasukkan ID item yang akan dikembalikan: ").strip()
    
    item = library.find_by_id(item_id)
    if item and not item.is_available:
        borrower = item.get_borrow_info()['borrowed_by']
        if library.return_item(item_id):
            print(f"\n✅ Berhasil mengembalikan item:")
            print(f"   {item}")
            print(f"   Dari: {borrower}")
        else:
            print(f"\n❌ Gagal mengembalikan item!")
    else:
        print(f"\n❌ Item tidak ditemukan atau tidak sedang dipinjam!")
    
    input("\nTekan Enter untuk melanjutkan...")

def remove_item_menu(library):
    # Menu untuk menghapus item
    print_header("HAPUS ITEM")
    item_id = input("Masukkan ID item yang akan dihapus: ").strip()
    
    item = library.find_by_id(item_id)
    
    if item:
        print(f"\nItem yang akan dihapus:")
        print(f"{item}")
        confirm = input("\nApakah Anda yakin? (y/n): ").strip().lower()
        
        if confirm == 'y':
            if library.remove_item(item_id):
                print(f"\n✅ Item berhasil dihapus!")
            else:
                print(f"\n❌ Gagal menghapus item!")
        else:
            print(f"\n❌ Penghapusan dibatalkan.")
    else:
        print(f"\n❌ Item dengan ID '{item_id}' tidak ditemukan!")
    
    input("\nTekan Enter untuk melanjutkan...")

def view_by_type_menu(library):
    # Menu untuk melihat item berdasarkan tipe
    print_header("LIHAT ITEM BERDASARKAN TIPE")
    print("1. Buku")
    print("2. Majalah")
    print("3. Koran")
    print("0. Kembali")
    
    choice = input("\nPilihan: ").strip()
    
    type_map = {
        "1": "Buku",
        "2": "Majalah",
        "3": "Koran"
    }
    
    if choice == "0":
        return
    
    if choice not in type_map:
        print("\n❌ Pilihan tidak valid!")
        input("\nTekan Enter untuk melanjutkan...")
        return
    
    item_type = type_map[choice]
    items = library.get_items_by_type(item_type)
    
    print(f"\n{'='*80}")
    print(f"DAFTAR {item_type.upper()}")
    print(f"{'='*80}")
    
    if items:
        print(f"Total: {len(items)} item\n")
        for idx, item in enumerate(items, 1):
            print(f"{idx}. {item}")
    else:
        print(f"Tidak ada {item_type.lower()} dalam koleksi.")
    
    print(f"{'='*80}")
    input("\nTekan Enter untuk melanjutkan...")

# Menginisialisasi data contoh untuk demonstrasi
def initialize_sample_data(library):
    # Buku
    book1 = Book("BK001", "Pemrograman Python untuk Pemula", 2023, "Dr. Ahmad Setiawan", 350, "978-1234567890")
    book2 = Book("BK002", "Machine Learning dengan Python", 2024, "Prof. Jane Smith", 480, "978-0987654321")
    book3 = Book("BK003", "Algoritma dan Struktur Data", 2022, "Dr. Robert Johnson", 420, "978-1122334455")
    book4 = Book("BK004", "Web Development Modern", 2024, "Sarah Williams", 390, "978-5566778899")
    book5 = Book("BK005", "Database Management Systems", 2023, "Michael Chen", 520, "978-9988776655")
    
    # Majalah
    mag1 = Magazine("MG001", "Tech Monthly Indonesia", 2024, "Tech Media Group", "November 2024", 145)
    mag2 = Magazine("MG002", "Science Today", 2024, "Science Publishing", "Oktober 2024", 218)
    mag3 = Magazine("MG003", "Programming World", 2024, "Dev Publisher", "November 2024", 89)
    
    # Koran
    news1 = Newspaper("NP001", "Kompas", 2024, "Kompas Gramedia", "2024-11-10")
    news2 = Newspaper("NP002", "Media Indonesia", 2024, "Media Group", "2024-11-10")
    news3 = Newspaper("NP003", "Republika", 2024, "Republika Media", "2024-11-09")
    
    # Tambahkan semua item
    items = [book1, book2, book3, book4, book5, mag1, mag2, mag3, news1, news2, news3]
    
    for item in items:
        library.add_item(item)
    
    # Simulasi beberapa peminjaman
    library.borrow_item("BK002", "Budi Santoso")
    library.borrow_item("MG001", "Andi Wijaya")
    library.borrow_item("NP001", "Siti Nurhaliza")

# Fungsi utama program
def main():
    # Inisialisasi perpustakaan
    library = Library("Perpustakaan ITERA")
    
    # Tambahkan data contoh
    print("Menginisialisasi data contoh...")
    initialize_sample_data(library)
    print("✅ Data berhasil dimuat!\n")
    input("Tekan Enter untuk melanjutkan...")
    
    # Main loop
    while True:
        clear_screen()
        print_menu()
        
        choice = input("Pilih menu (0-11): ").strip()
        
        if choice == "0":
            print("\n" + "="*80)
            print("Terima kasih telah menggunakan Sistem Manajemen Perpustakaan ITERA!")
            print("="*80 + "\n")
            break
            
        elif choice == "1":
            add_item_menu(library)
            
        elif choice == "2":
            clear_screen()
            library.display_all_items()
            input("\nTekan Enter untuk melanjutkan...")
            
        elif choice == "3":
            clear_screen()
            library.display_available_items()
            input("\nTekan Enter untuk melanjutkan...")
            
        elif choice == "4":
            clear_screen()
            print_header("ITEM YANG SEDANG DIPINJAM")
            borrowed = library.get_borrowed_items()
            if borrowed:
                print(f"Total: {len(borrowed)} item\n")
                for idx, item in enumerate(borrowed, 1):
                    borrow_info = item.get_borrow_info()
                    print(f"{idx}. {item}")
                    print(f"   Dipinjam oleh: {borrow_info['borrowed_by']} | Tanggal: {borrow_info['borrow_date']}\n")
            else:
                print("Tidak ada item yang sedang dipinjam.")
            input("\nTekan Enter untuk melanjutkan...")
            
        elif choice == "5":
            search_by_id_menu(library)
            
        elif choice == "6":
            search_by_title_menu(library)
            
        elif choice == "7":
            borrow_item_menu(library)
            
        elif choice == "8":
            return_item_menu(library)
            
        elif choice == "9":
            remove_item_menu(library)
            
        elif choice == "10":
            clear_screen()
            library.display_statistics()
            input("\nTekan Enter untuk melanjutkan...")
            
        elif choice == "11":
            view_by_type_menu(library)
            
        else:
            print("\n❌ Pilihan tidak valid! Silakan pilih menu 0-11.")
            input("\nTekan Enter untuk melanjutkan...")

if __name__ == "__main__":
    main()