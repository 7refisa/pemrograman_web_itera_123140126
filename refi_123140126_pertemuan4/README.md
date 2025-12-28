Program Python untuk mengelola dan menganalisis data nilai mahasiswa dengan berbagai fitur pengolahan data.

## Deskripsi
Program ini merupakan aplikasi berbasis console yang memungkinkan pengguna untuk mengelola data nilai mahasiswa, menghitung nilai akhir, menentukan grade, dan melakukan berbagai analisis data seperti mencari nilai tertinggi/terendah, filtering berdasarkan grade, dan menghitung rata-rata kelas.

## Fitur Utama
1. **Tampilkan Data Mahasiswa**
   - Menampilkan seluruh data mahasiswa dalam format tabel yang rapi
   - Menampilkan NIM, Nama, Nilai UTS, UAS, Tugas, Nilai Akhir, dan Grade

2. **Tambah Data Mahasiswa**
   - Menambahkan mahasiswa baru ke dalam database
   - Validasi input untuk nilai (0-100)
   - Validasi NIM agar tidak duplikat
   - Otomatis menghitung nilai akhir dan grade

3. **Cari Nilai Tertinggi & Terendah**
   - Mencari mahasiswa dengan nilai akhir tertinggi
   - Mencari mahasiswa dengan nilai akhir terendah
   - Menampilkan detail lengkap mahasiswa tersebut

4. **Filter Berdasarkan Grade**
   - Memfilter dan menampilkan mahasiswa berdasarkan grade tertentu (A/B/C/D/E)
   - Menampilkan hasil dalam format tabel

5. **Hitung Rata-rata Nilai Kelas**
   - Menghitung rata-rata nilai akhir seluruh kelas
   - Menampilkan jumlah mahasiswa dan total nilai

## Sistem Penilaian
### Bobot Nilai
- UTS: 30%
- UAS: 40%
- Tugas: 30%

### Rumus Nilai Akhir
```
Nilai Akhir = (0.3 × UTS) + (0.4 × UAS) + (0.3 × Tugas)
```

### Grade
| Grade | Rentang Nilai |
| ----- | ------------- |
| A     | ≥ 80          |
| B     | ≥ 70          |
| C     | ≥ 60          |
| D     | ≥ 50          |
| E     | < 50          |

## Cara Menjalankan Program
### Langkah-langkah
1. Clone atau download repository ini
2. Buka terminal/command prompt
3. Navigasi ke folder `refi_123140126_pertemuan4`
4. Jalankan program dengan command:
   ```bash
   python dataMahasiswa.py
   ```

## Penggunaan
Setelah program dijalankan, akan muncul menu utama:

```
PROGRAM PENGELOLAAN DATA NILAI MAHASISWA
========================================

--- MENU UTAMA ---
1. Tampilkan Semua Data Mahasiswa
2. Tambah Data Mahasiswa
3. Cari Nilai Tertinggi & Terendah
4. Filter Mahasiswa Berdasarkan Grade
5. Hitung Rata-rata Nilai Kelas
0. Keluar Program
```

Pilih menu dengan memasukkan angka (0-5) sesuai kebutuhan.

## Struktur Program
### Data Awal
Program dilengkapi dengan 6 data mahasiswa awal:
- Harry Potter (NIM: 101)
- Hermione Granger (NIM: 102)
- Ron Weasley (NIM: 103)
- Draco Malfoy (NIM: 104)
- Luna Lovegood (NIM: 105)
- Neville Longbottom (NIM: 106)

### Fungsi Utama
| Fungsi                      | Deskripsi                                                      |
| --------------------------- | -------------------------------------------------------------- |
| `hitung_nilai_akhir()`      | Menghitung nilai akhir berdasarkan bobot                       |
| `tentukan_grade()`          | Menentukan grade dari nilai akhir                              |
| `proses_semua_data()`       | Memproses seluruh data untuk menambahkan nilai akhir dan grade |
| `tampilkan_data()`          | Menampilkan data dalam format tabel                            |
| `tambah_data_mahasiswa()`   | Menambahkan mahasiswa baru                                     |
| `cari_tertinggi_terendah()` | Mencari nilai tertinggi dan terendah                           |
| `filter_by_grade()`         | Memfilter mahasiswa berdasarkan grade                          |
| `rata_rata_kelas()`         | Menghitung rata-rata nilai kelas                               |

## Contoh Output
### Tampilan Tabel Data
```
PROGRAM PENGELOLAAN DATA NILAI MAHASISWA
============================================================================
| No  | NIM        | Nama Mahasiswa       | UTS   | UAS   | Tugas | Akhir  | Grade |
----------------------------------------------------------------------------
| 1   | 101        | Harry Potter         |    80 |    85 |    90 |  85.50 |   A   |
| 2   | 102        | Hermione Granger     |    95 |    98 |   100 |  97.60 |   A   |
...
```