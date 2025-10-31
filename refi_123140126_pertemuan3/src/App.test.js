import { render, screen, fireEvent } from "@testing-library/react";
import { MemoryRouter } from "react-router-dom";
import { BookProvider, useBooks } from "../../src/context/BookContext";
import App from "../../src/App";
import Home from "../../src/pages/Home/Home";
import Stats from "../../src/pages/Stats/Stats";
import { useBookStats } from "../../src/hooks/useBookStats";

// 1. Mock data dan context
const mockBooks = [
  { id: "1", title: "Bumi", author: "Tere Liye", status: "milik" },
  { id: "2", title: "Laskar Pelangi", author: "Andrea Hirata", status: "baca" },
  { id: "3", title: "Atomic Habits", author: "James Clear", status: "beli" },
];

// Mock kustom hook useBooks
jest.mock("./context/BookContext", () => ({
  ...jest.requireActual("./context/BookContext"),
  useBooks: jest.fn(),
}));

// Mock kustom hook useBookStats
jest.mock("./hooks/useBookStats", () => ({
  useBookStats: jest.fn(),
}));

// Wrapper kustom untuk render dengan provider
const renderWithProviders = (ui, { providerProps, ...renderOptions }) => {
  return render(
    <MemoryRouter>
      <BookProvider {...providerProps}>{ui}</BookProvider>
    </MemoryRouter>,
    renderOptions
  );
};

describe("Aplikasi Manajemen Buku", () => {
  // Setup mock sebelum setiap tes
  beforeEach(() => {
    useBooks.mockReturnValue({
      books: mockBooks,
      addBook: jest.fn(),
      deleteBook: jest.fn(),
      updateBook: jest.fn(),
    });

    useBookStats.mockReturnValue({
      total: 3,
      owned: 1,
      reading: 1,
      toBuy: 1,
    });
  });

  // Test 1: Render Halaman Home dan tampilkan buku
  test("Render Halaman Home dan tampilkan daftar buku", () => {
    renderWithProviders(<Home />);

    // Cek apakah judul buku tampil
    expect(screen.getByText("Bumi")).toBeInTheDocument();
    expect(screen.getByText("Laskar Pelangi")).toBeInTheDocument();
    expect(screen.getByText("Atomic Habits")).toBeInTheDocument();
  });

  // Test 2: Pencarian (Search)
  test("Filter pencarian berfungsi di Halaman Home", () => {
    renderWithProviders(<Home />);

    // Dapatkan input pencarian
    const searchInput = screen.getByPlaceholderText(
      "Cari berdasarkan judul atau penulis..."
    );

    fireEvent.change(searchInput, { target: { value: "Bumi" } });

    expect(screen.getByText("Bumi")).toBeInTheDocument();
    expect(screen.queryByText("Laskar Pelangi")).not.toBeInTheDocument();
    expect(screen.queryByText("Atomic Habits")).not.toBeInTheDocument();
  });

  // Test 3: Filter Status
  test("Filter status berfungsi di Halaman Home", () => {
    renderWithProviders(<Home />);

    fireEvent.click(screen.getByText("Dibaca"));

    expect(screen.queryByText("Bumi")).not.toBeInTheDocument();
    expect(screen.getByText("Laskar Pelangi")).toBeInTheDocument();
    expect(screen.queryByText("Atomic Habits")).not.toBeInTheDocument();
  });

  // Test 4: Render Halaman Statistik
  test("Render Halaman Statistik dan tampilkan data", () => {
    renderWithProviders(<Stats />);

    // Cek apakah statistik dari mock hook tampil
    expect(screen.getByText("Total Buku")).toBeInTheDocument();
    expect(screen.getByText("3")).toBeInTheDocument(); // Total
    expect(screen.getByText("Dimiliki")).toBeInTheDocument();
    expect(screen.getByText("1")).toBeInTheDocument(); // Owned
    expect(screen.getByText("Sedang Dibaca")).toBeInTheDocument();
    const readingValue = screen.getAllByText("1")[1];
    expect(readingValue).toBeInTheDocument(); // Reading
  });

  // Test 5: Navigasi aplikasi
  test("Navigasi dari Home ke Stats berfungsi", () => {
    render(
      <MemoryRouter initialEntries={["/"]}>
        <BookProvider>
          <App />
        </BookProvider>
      </MemoryRouter>
    );

    // Awalnya di Home
    expect(screen.getByText("Daftar Buku Saya")).toBeInTheDocument();

    // Klik link 'Statistik'
    fireEvent.click(screen.getByText("Statistik"));

    // Pindah ke halaman Stats
    expect(screen.getByText("Statistik Buku Anda")).toBeInTheDocument();
    expect(screen.queryByText("Daftar Buku Saya")).not.toBeInTheDocument();
  });
});
