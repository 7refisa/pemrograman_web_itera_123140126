import React, { useState, useMemo } from "react";
import { useBooks } from "../../context/BookContext";
import BookList from "../../components/BookList/BookList";
import BookFilter from "../../components/BookFilter/BookFilter";
import BookForm from "../../components/BookForm/BookForm";
import "./Home.css";

function Modal({ isOpen, onClose, children }) {
  if (!isOpen) return null;

  return (
    <>
      <div className="modal-overlay" onClick={onClose} />
      <div className="modal-content">
        <button className="modal-close-btn" onClick={onClose}>
          &times;
        </button>
        {children}
      </div>
    </>
  );
}

function Home() {
  const { books } = useBooks();

  const [searchTerm, setSearchTerm] = useState("");
  const [filterStatus, setFilterStatus] = useState("semua");

  const [isModalOpen, setIsModalOpen] = useState(false);
  const [bookToEdit, setBookToEdit] = useState(null);

  const filteredBooks = useMemo(() => {
    return books.filter((book) => {
      const statusMatch =
        filterStatus === "semua" || book.status === filterStatus;

      const searchMatch =
        book.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
        book.author.toLowerCase().includes(searchTerm.toLowerCase());

      return statusMatch && searchMatch;
    });
  }, [books, searchTerm, filterStatus]);

  const handleAddBookClick = () => {
    setBookToEdit(null);
    setIsModalOpen(true);
  };

  const handleEditBook = (book) => {
    setBookToEdit(book);
    setIsModalOpen(true);
  };

  const handleCloseModal = () => {
    setIsModalOpen(false);
    setBookToEdit(null);
  };

  return (
    <div className="home-page">
      <div className="home-header">
        <h2>Daftar Buku Saya</h2>
        <button className="btn-primary" onClick={handleAddBookClick}>
          + Tambah Buku Baru
        </button>
      </div>

      <BookFilter
        searchTerm={searchTerm}
        setSearchTerm={setSearchTerm}
        filterStatus={filterStatus}
        setFilterStatus={setFilterStatus}
      />

      <BookList books={filteredBooks} onEditBook={handleEditBook} />

      <Modal isOpen={isModalOpen} onClose={handleCloseModal}>
        <BookForm bookToEdit={bookToEdit} onFormSubmit={handleCloseModal} />
      </Modal>
    </div>
  );
}

export default Home;
