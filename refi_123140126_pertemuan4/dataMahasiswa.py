import os

data_mahasiswa = [
    {'nama': 'Harry Potter', 'NIM': '101', 'nilai_uts': 80, 'nilai_uas': 85, 'nilai_tugas': 90},
    {'nama': 'Hermione Granger', 'NIM': '102', 'nilai_uts': 95, 'nilai_uas': 98, 'nilai_tugas': 100},
    {'nama': 'Ron Weasley', 'NIM': '103', 'nilai_uts': 50, 'nilai_uas': 60, 'nilai_tugas': 55},
    {'nama': 'Draco Malfoy', 'NIM': '104', 'nilai_uts': 85, 'nilai_uas': 88, 'nilai_tugas': 82},
    {'nama': 'Luna Lovegood', 'NIM': '105', 'nilai_uts': 78, 'nilai_uas': 75, 'nilai_tugas': 80},
    {'nama': 'Neville Longbottom', 'NIM': '106', 'nilai_uts': 45, 'nilai_uas': 65, 'nilai_tugas': 50},
]

def hitung_nilai_akhir(uts, uas, tugas):
    """
    Menghitung nilai akhir berdasarkan bobot yang ditentukan.
    (30% UTS + 40% UAS + 30% Tugas)
    """
    return (0.3 * uts) + (0.4 * uas) + (0.3 * tugas)

def tentukan_grade(nilai_akhir):
    """
    Menentukan grade berdasarkan nilai akhir.
    A: ≥80, B: ≥70, C: ≥60, D: ≥50, E: <50
    """
    if nilai_akhir >= 80:
        return 'A'
    elif nilai_akhir >= 70:
        return 'B'
    elif nilai_akhir >= 60:
        return 'C'
    elif nilai_akhir >= 50:
        return 'D'
    else:
        return 'E'

def proses_semua_data(data_list):
    """
    Memproses seluruh data dalam list untuk menambahkan
    'nilai_akhir' dan 'grade' ke setiap dictionary mahasiswa.
    """
    for mhs in data_list:
        mhs['nilai_akhir'] = hitung_nilai_akhir(mhs['nilai_uts'], mhs['nilai_uas'], mhs['nilai_tugas'])
        mhs['grade'] = tentukan_grade(mhs['nilai_akhir'])
    return data_list

def tampilkan_data(data_list):
    """
    Menampilkan data mahasiswa dalam format tabel yang rapi.
    """
    # Membersihkan layar konsol
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("PROGRAM PENGELOLAAN DATA NILAI MAHASISWA")
    print("=" * 76)
    # Header Tabel
    print(f"| {'No':<3} | {'NIM':<10} | {'Nama Mahasiswa':<20} | {'UTS':<5} | {'UAS':<5} | {'Tugas':<5} | {'Akhir':<6} | {'Grade':<5} |")
    print("-" * 76)
    
    # Body Tabel
    if not data_list:
        print(f"| {'':<74} |")
        print(f"| {'Tidak ada data untuk ditampilkan.':^74} |")
        print(f"| {'':<74} |")
    else:
        for i, mhs in enumerate(data_list, 1):
            print(f"| {i:<3} | {mhs['NIM']:<10} | {mhs['nama']:<20} | {mhs['nilai_uts']:>5} | {mhs['nilai_uas']:>5} | {mhs['nilai_tugas']:>5} | {mhs['nilai_akhir']:>6.2f} | {mhs['grade']:^5} |")
    
    print("-" * 76)

def input_nilai_valid(prompt):
    """Helper function untuk memastikan input nilai adalah angka (0-100)."""
    while True:
        try:
            nilai = float(input(prompt))
            if 0 <= nilai <= 100:
                return nilai
            else:
                print("Error: Nilai harus berada di antara 0 dan 100.")
        except ValueError:
            print("Error: Masukkan harus berupa angka.")

def tambah_data_mahasiswa(data_list):
    """
    Menambahkan data mahasiswa baru ke dalam list utama.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    print("--- TAMBAH DATA MAHASISWA ---")
    
    nama = input("Masukkan Nama   : ")
    nim = input("Masukkan NIM    : ")
    
    # Validasi NIM agar unik
    while any(mhs['NIM'] == nim for mhs in data_list):
        print("Error: NIM sudah ada. Harap masukkan NIM yang unik.")
        nim = input("Masukkan NIM    : ")
        
    uts = input_nilai_valid("Masukkan Nilai UTS: ")
    uas = input_nilai_valid("Masukkan Nilai UAS: ")
    tugas = input_nilai_valid("Masukkan Nilai Tugas: ")
    
    # Membuat dictionary baru dan memprosesnya
    mahasiswa_baru = {
        'nama': nama,
        'NIM': nim,
        'nilai_uts': uts,
        'nilai_uas': uas,
        'nilai_tugas': tugas
    }
    
    # Langsung hitung nilai akhir dan grade
    mahasiswa_baru['nilai_akhir'] = hitung_nilai_akhir(uts, uas, tugas)
    mahasiswa_baru['grade'] = tentukan_grade(mahasiswa_baru['nilai_akhir'])
    
    # Tambahkan ke list utama
    data_list.append(mahasiswa_baru)
    print("\nData mahasiswa baru berhasil ditambahkan!")

def cari_tertinggi_terendah(data_list):
    """
    Mencari dan menampilkan mahasiswa dengan nilai akhir tertinggi dan terendah.
    """
    if not data_list:
        print("Data masih kosong.")
        return

    # Menggunakan fungsi max() dan min() dengan lambda key
    tertinggi = max(data_list, key=lambda mhs: mhs['nilai_akhir'])
    terendah = min(data_list, key=lambda mhs: mhs['nilai_akhir'])
    
    print("\n--- NILAI TERTINGGI & TERENDAH ---")
    print(f"Nilai Tertinggi diraih oleh: {tertinggi['nama']} (NIM: {tertinggi['NIM']})")
    print(f"   -> Nilai Akhir: {tertinggi['nilai_akhir']:.2f} (Grade: {tertinggi['grade']})")
    
    print(f"\nNilai Terendah diraih oleh : {terendah['nama']} (NIM: {terendah['NIM']})")
    print(f"   -> Nilai Akhir: {terendah['nilai_akhir']:.2f} (Grade: {terendah['grade']})")

def filter_by_grade(data_list):
    """
    Memfilter dan menampilkan mahasiswa berdasarkan grade yang diinput.
    """
    print("\n--- FILTER BERDASARKAN GRADE ---")
    grade_dicari = input("Masukkan Grade yang ingin dicari (A/B/C/D/E): ").upper()
    
    if grade_dicari not in ['A', 'B', 'C', 'D', 'E']:
        print("Error: Grade tidak valid.")
        return
        
    # Menggunakan list comprehension untuk memfilter
    filtered_list = [mhs for mhs in data_list if mhs['grade'] == grade_dicari]
    
    print(f"\nMenampilkan data untuk Grade: {grade_dicari}")
    tampilkan_data(filtered_list)

def rata_rata_kelas(data_list):
    """
    Menghitung dan menampilkan rata-rata nilai akhir seluruh kelas.
    """
    if not data_list:
        print("Data masih kosong.")
        return
        
    total_nilai = sum(mhs['nilai_akhir'] for mhs in data_list)
    rata_rata = total_nilai / len(data_list)
    
    print("\n--- RATA-RATA NILAI KELAS ---")
    print(f"Jumlah Mahasiswa : {len(data_list)}")
    print(f"Total Nilai Kelas: {total_nilai:.2f}")
    print(f"Rata-rata Kelas  : {rata_rata:.2f}")

# --- 3. FUNGSI UTAMA (MAIN MENU) ---

def tampilkan_menu():
    """Helper function untuk membersihkan layar dan menampilkan menu."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print("PROGRAM PENGELOLAAN DATA NILAI MAHASISWA")
    print("=" * 40)
    print("\n--- MENU UTAMA ---")
    print("1. Tampilkan Semua Data Mahasiswa")
    print("2. Tambah Data Mahasiswa")
    print("3. Cari Nilai Tertinggi & Terendah")
    print("4. Filter Mahasiswa Berdasarkan Grade")
    print("5. Hitung Rata-rata Nilai Kelas")
    print("0. Keluar Program")

def main():
    """
    Fungsi utama yang menjalankan menu program.
    """
    # Memproses data awal saat program pertama kali dijalankan
    data_list = proses_semua_data(data_mahasiswa)
    
    while True:
        tampilkan_menu()
        
        pilihan = input("\nMasukkan pilihan Anda (0-5): ")
        
        if pilihan == '1':
            tampilkan_data(data_list) 
            
        elif pilihan == '2':
            tambah_data_mahasiswa(data_list)
            print("\nMenampilkan tabel data terbaru...")
            tampilkan_data(data_list)
            
        elif pilihan == '3':
            tampilkan_data(data_list) 
            cari_tertinggi_terendah(data_list)
            
        elif pilihan == '4':
            filter_by_grade(data_list)
            
        elif pilihan == '5':
            tampilkan_data(data_list)
            rata_rata_kelas(data_list)
            
        elif pilihan == '0':
            print("\nTerima kasih telah menggunakan program ini. Sampai jumpa!")
            break
            
        else:
            print("\nError: Pilihan tidak valid. Silakan coba lagi.")

        if pilihan != '0':
             input("\nTekan Enter untuk kembali ke menu...")

if __name__ == "__main__":
    main()