import React from "react";
import { useBooks } from "../../context/BookContext";
import "./BookList.css";

function BookItem({ book, onEdit }) {
  const { deleteBook } = useBooks();

  const getStatusBadge = (status) => {
    switch (status) {
      case "milik":
        return <span className="badge badge-owned">Dimiliki</span>;
      case "baca":
        return <span className="badge badge-reading">Sedang Dibaca</span>;
      case "beli":
        return <span className="badge badge-tobuy">Akan Dibeli</span>;
      default:
        return <span className="badge">{status}</span>;
    }
  };

  return (
    <li className="book-item">
      <div className="book-item-info">
        <h3>{book.title}</h3>
        <p>oleh {book.author}</p>
      </div>
      <div className="book-item-status">{getStatusBadge(book.status)}</div>
      <div className="book-item-actions">
        <button className="btn-edit" onClick={() => onEdit(book)}>
          Edit
        </button>
        <button className="btn-danger" onClick={() => deleteBook(book.id)}>
          Hapus
        </button>
      </div>
    </li>
  );
}

function BookList({ books, onEditBook }) {
  if (books.length === 0) {
    return (
      <p className="empty-list-message">
        Tidak ada buku yang cocok dengan kriteria Anda.
      </p>
    );
  }

  return (
    <ul className="book-list">
      {books.map((book) => (
        <BookItem key={book.id} book={book} onEdit={onEditBook} />
      ))}
    </ul>
  );
}

export default BookList;
