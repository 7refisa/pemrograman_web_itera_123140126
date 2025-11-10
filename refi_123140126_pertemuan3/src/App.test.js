// [PERBAIKAN 1] Import ini ditambahkan untuk memperbaiki '.toBeInTheDocument() is not a function'
import '@testing-library/jest-dom';
import { render, screen, fireEvent, act } from '@testing-library/react';
import { MemoryRouter } from 'react-router-dom';
import { BookProvider, useBooks } from './context/BookContext';
import { useBookStats } from './hooks/useBookStats';
import App from './App';
import Home from './pages/Home/Home';
import Stats from './pages/Stats/Stats';

// 1. Mock data dan context
const mockBooks = [
  { id: 1, title: 'Buku A', author: 'Penulis A', status: 'Dimiliki' },
  // [PERBAIKAN FINAL] Status dikembalikan ke "Sedang Dibaca"
  // agar cocok dengan value dari tombol filter di BookFilter.js
  { id: 2, title: 'Buku B', author: 'Penulis B', status: 'Sedang Dibaca' },
  { id: 3, title: 'Buku C', author: 'Penulis C', status: 'Akan Dibeli' },
];

// 2. Mock custom hook useBookStats
// Kita mock 'useBookStats' agar mengembalikan data palsu
jest.mock('./hooks/useBookStats', () => ({
  useBookStats: () => ({
    totalBooks: 3,
    owned: 1,
    reading: 1, // Nama properti ini 'reading'
    toBuy: 1,
  }),
}));

// 3. Mock custom hook useBooks
// Kita mock 'useBooks' agar mengembalikan data palsu
jest.mock('./context/BookContext', () => ({
  // ... kita pertahankan implementasi aslinya (seperti BookProvider)
  ...jest.requireActual('./context/BookContext'),
  // Tapi kita override 'useBooks'
  useBooks: () => ({
    books: mockBooks,
    addBook: jest.fn(),
    editBook: jest.fn(),
    deleteBook: jest.fn(),
  }),
}));

// [PERBAIKAN 2] Menambahkan '= {}' sebagai nilai default
// Ini memperbaiki error "Cannot destructure property 'providerProps'"
const renderWithProviders = (ui, { providerProps, ...renderOptions } = {}) => {
  return render(
    <MemoryRouter>
      <BookProvider {...providerProps}>{ui}</BookProvider>
    </MemoryRouter>,
    renderOptions
  );
};

// 4. Mulai Testing
describe('Aplikasi Manajemen Buku', () => {
  
  test('Render Halaman Home dan tampilkan daftar buku', () => {
    renderWithProviders(<Home />); // Sekarang aman dipanggil tanpa argumen kedua

    // Cek apakah judul halaman muncul
    expect(screen.getByText('Daftar Buku Saya')).toBeInTheDocument();
    
    // Cek apakah mock data buku muncul
    expect(screen.getByText('Buku A')).toBeInTheDocument();
    expect(screen.getByText('Buku B')).toBeInTheDocument();
    expect(screen.getByText('Buku C')).toBeInTheDocument();
  });

  test('Filter pencarian berfungsi di Halaman Home', () => {
    renderWithProviders(<Home />);
    
    // Cari buku 'A'
    const searchInput = screen.getByPlaceholderText(/Cari berdasarkan judul atau penulis/i);
    fireEvent.change(searchInput, { target: { value: 'Buku A' } });

    // Buku A harus ada
    expect(screen.getByText('Buku A')).toBeInTheDocument();
    // Buku B dan C harus hilang
    expect(screen.queryByText('Buku B')).not.toBeInTheDocument();
    expect(screen.queryByText('Buku C')).not.toBeInTheDocument();
  });

  // Tes 'Filter status berfungsi di Halaman Home' yang error
  // telah dihapus sesuai permintaan.

  test('Render Halaman Statistik dan tampilkan data', () => {
    renderWithProviders(<Stats />);

    // [PERBAIKAN 3] Mencari teks yang benar sesuai HTML dump
    expect(screen.getByText('Statistik Buku Anda')).toBeInTheDocument();

    // Cek apakah data dari useBookStats (yang sudah di-mock) muncul
    expect(screen.getByText('Total Buku')).toBeInTheDocument();
    
    expect(screen.getByText('Dimiliki')).toBeInTheDocument();
    expect(screen.getByText('Sedang Dibaca')).toBeInTheDocument();
    expect(screen.getByText('Akan Dibeli')).toBeInTheDocument();

    // [PERBAIKAN ERROR GAGAL 2]
    // Kita cari SEMUA elemen yang bertuliskan '1'
    const allCounts = screen.getAllByText('1');
    // Kita pastikan jumlahnya ada 3 (untuk Dimiliki, Dibaca, Akan Dibeli)
    expect(allCounts.length).toBe(3);
  });

  test('Navigasi dari Home ke Stats berfungsi', () => {
    // Untuk tes navigasi, kita render App lengkap
    render(
      <MemoryRouter initialEntries={['/']}>
        <BookProvider>
          <App />
        </BookProvider>
      </MemoryRouter>
    );

    // Awalnya di Home
    expect(screen.getByText('Daftar Buku Saya')).toBeInTheDocument();

    // Klik link 'Statistik'
    fireEvent.click(screen.getByText('Statistik'));

    // [PERBAIKAN 3] Mencari teks yang benar sesuai HTML dump
    expect(screen.getByText('Statistik Buku Anda')).toBeInTheDocument();
    expect(screen.queryByText('Daftar Buku Saya')).not.toBeInTheDocument();

    // Klik link 'Home'
    fireEvent.click(screen.getByText('Home'));
    
    // Cek apakah kembali ke Home
    expect(screen.getByText('Daftar Buku Saya')).toBeInTheDocument();
  });
});
