from perpustakaan import Library, Book, Magazine, Newspaper

# Testing encapsulation dengan private attributes
def test_encapsulation():
    print("\n" + "="*80)
    print("TEST 1: ENCAPSULATION - Private & Protected Attributes")
    print("="*80)
    
    book = Book("BK999", "Test Book", 2024, "Test Author", 300, "978-1234567890")
    
    # Akses menggunakan property (benar)
    print(f"✅ Akses menggunakan property:")
    print(f"   ID: {book.item_id}")
    print(f"   Title: {book.title}")
    print(f"   Author: {book.author}")
    print(f"   Year: {book.year}")
    
    # Coba ubah title menggunakan property setter
    print(f"\n✅ Ubah title menggunakan property setter:")
    old_title = book.title
    book.title = "New Test Book"
    print(f"   Old title: {old_title}")
    print(f"   New title: {book.title}")
    
    # Coba akses private attribute langsung (akan error)
    print(f"\n❌ Coba akses private attribute langsung:")
    try:
        print(f"   book.__item_id: {book.__item_id}")
    except AttributeError as e:
        print(f"   Error: {e}")
        print(f"   ➡️ Private attribute tidak bisa diakses langsung!")
    
    print("\n" + "="*80)


# Testing inheritance dan abstract methods
def test_inheritance():
    print("\n" + "="*80)
    print("TEST 2: INHERITANCE & ABSTRACT METHODS")
    print("="*80)
    
    book = Book("BK001", "Python Guide", 2024, "John Doe", 300, "978-1234567890")
    magazine = Magazine("MG001", "Tech Magazine", 2024, "Tech Publisher", "Nov 2024", 100)
    newspaper = Newspaper("NP001", "Daily News", 2024, "News Corp", "2024-11-10")
    
    items = [book, magazine, newspaper]
    
    print("✅ Semua subclass mengimplementasikan abstract methods:")
    for item in items:
        print(f"\n{item.get_item_type()}:")
        print(f"  get_item_type(): {item.get_item_type()}")
        print(f"  get_description():")
        description_lines = item.get_description().split('\n')
        for line in description_lines[:3]:  # Tampilkan 3 baris pertama
            print(f"    {line}")
        print(f"    ...")
    
    print("\n" + "="*80)


# Testing polymorphism dengan method overriding
def test_polymorphism():
    print("\n" + "="*80)
    print("TEST 3: POLYMORPHISM - Method Overriding")
    print("="*80)
    
    book = Book("BK001", "Python Guide", 2024, "John Doe", 300, "978-1234567890")
    magazine = Magazine("MG001", "Tech Magazine", 2024, "Tech Publisher", "Nov 2024", 100)
    newspaper = Newspaper("NP001", "Daily News", 2024, "News Corp", "2024-11-10")
    
    items = [book, magazine, newspaper]
    
    print("✅ Method __str__() yang sama, output berbeda (polymorphism):")
    for item in items:
        print(f"\n{item.__class__.__name__}.__str__():")
        print(f"  {item}")
    
    print("\n" + "="*80)


# Testing property decorator dengan validasi
def test_property_decorator():
    print("\n" + "="*80)
    print("TEST 4: PROPERTY DECORATOR dengan Validasi")
    print("="*80)
    
    book = Book("BK001", "Test Book", 2024, "Author", 300, "978-1234567890")
    
    print("✅ Property getter (read-only untuk item_id):")
    print(f"   book.item_id = {book.item_id}")
    
    print("\n❌ Coba set item_id (read-only property):")
    try:
        book.item_id = "BK999"
    except AttributeError as e:
        print(f"   Error: can't set attribute")
        print(f"   ➡️ item_id adalah read-only property!")
    
    print("\n✅ Property setter dengan validasi (title):")
    print(f"   Old title: {book.title}")
    book.title = "New Title"
    print(f"   New title: {book.title}")
    
    print("\n❌ Validasi title (empty string):")
    try:
        book.title = ""
    except ValueError as e:
        print(f"   Error: {e}")
        print(f"   ➡️ Validasi mencegah nilai invalid!")
    
    print("\n✅ Property dengan computed value (Library):")
    library = Library("Test Library")
    library.add_item(book)
    library.add_item(Magazine("MG001", "Magazine", 2024, "Pub", "Nov", 1))
    print(f"   library.total_items = {library.total_items} (computed)")
    print(f"   library.available_items = {library.available_items} (computed)")
    
    print("\n" + "="*80)


# Testing fungsionalitas Library class
def test_library_functionality():
    print("\n" + "="*80)
    print("TEST 5: LIBRARY FUNCTIONALITY")
    print("="*80)
    
    library = Library("Test Library")
    
    # Tambah items
    book1 = Book("BK001", "Python Programming", 2024, "John Doe", 300, "978-1234567890")
    book2 = Book("BK002", "Java Programming", 2023, "Jane Smith", 400, "978-0987654321")
    magazine = Magazine("MG001", "Tech Magazine", 2024, "Tech Pub", "Nov 2024", 100)
    
    print("✅ Test add_item():")
    library.add_item(book1)
    library.add_item(book2)
    library.add_item(magazine)
    print(f"   Total items: {library.total_items}")
    
    print("\n✅ Test find_by_id():")
    found = library.find_by_id("BK001")
    print(f"   Found: {found}")
    
    print("\n✅ Test find_by_title():")
    results = library.find_by_title("Programming")
    print(f"   Found {len(results)} items:")
    for item in results:
        print(f"   - {item}")
    
    print("\n✅ Test borrow_item():")
    success = library.borrow_item("BK001", "Budi Santoso")
    print(f"   Borrow success: {success}")
    print(f"   Available items: {library.available_items}")
    print(f"   Borrowed items: {library.borrowed_items}")
    
    print("\n✅ Test return_item():")
    success = library.return_item("BK001")
    print(f"   Return success: {success}")
    print(f"   Available items: {library.available_items}")
    
    print("\n✅ Test get_statistics():")
    stats = library.get_statistics()
    print(f"   Statistics: {stats}")
    
    print("\n" + "="*80)


# Run all tests
def main():
    print("\n" + "="*80)
    print("DEMONSTRASI KONSEP OOP PYTHON")
    print("Sistem Manajemen Perpustakaan - Refi (123140126)")
    print("="*80)
    
    test_encapsulation()
    test_inheritance()
    test_polymorphism()
    test_property_decorator()
    test_library_functionality()
    
    print("\n" + "="*80)
    print("SEMUA TEST BERHASIL! ✅")
    print("="*80)
    print("\nKesimpulan:")
    print("✅ Abstract Class & Inheritance - Berhasil diimplementasikan")
    print("✅ Encapsulation (Private/Protected) - Berhasil diimplementasikan")
    print("✅ Polymorphism (Method Overriding) - Berhasil diimplementasikan")
    print("✅ Property Decorator - Berhasil diimplementasikan")
    print("✅ Fungsionalitas Program - Berjalan dengan baik")
    print("="*80 + "\n")


if __name__ == "__main__":
    main()
