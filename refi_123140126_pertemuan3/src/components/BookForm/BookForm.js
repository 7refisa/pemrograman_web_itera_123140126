import React, { useState, useEffect } from "react";
import { useBooks } from "../../context/BookContext";
import "./BookForm.css";

function BookForm({ bookToEdit, onFormSubmit }) {
  const { addBook, updateBook } = useBooks();

  const [title, setTitle] = useState("");
  const [author, setAuthor] = useState("");
  const [status, setStatus] = useState("milik");

  const [errors, setErrors] = useState({});

  useEffect(() => {
    if (bookToEdit) {
      setTitle(bookToEdit.title);
      setAuthor(bookToEdit.author);
      setStatus(bookToEdit.status);
    } else {
      setTitle("");
      setAuthor("");
      setStatus("milik");
    }
  }, [bookToEdit]);

  /**
   * @returns {boolean}
   */
  const validateForm = () => {
    const newErrors = {};
    if (!title.trim()) {
      newErrors.title = "Judul tidak boleh kosong";
    }
    if (!author.trim()) {
      newErrors.author = "Penulis tidak boleh kosong";
    }
    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!validateForm()) {
      return;
    }

    const bookData = { title, author, status };

    if (bookToEdit) {
      updateBook({ ...bookData, id: bookToEdit.id });
    } else {
      addBook(bookData);
    }

    onFormSubmit();
  };

  return (
    <form onSubmit={handleSubmit} className="book-form">
      <h3>{bookToEdit ? "Edit Buku" : "Tambah Buku Baru"}</h3>

      <div className="form-group">
        <label htmlFor="title">Judul Buku</label>
        <input
          type="text"
          id="title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          aria-invalid={errors.title ? "true" : "false"}
        />
        {errors.title && <span className="error-message">{errors.title}</span>}
      </div>

      <div className="form-group">
        <label htmlFor="author">Penulis</label>
        <input
          type="text"
          id="author"
          value={author}
          onChange={(e) => setAuthor(e.target.value)}
          aria-invalid={errors.author ? "true" : "false"}
        />
        {errors.author && (
          <span className="error-message">{errors.author}</span>
        )}
      </div>

      <div className="form-group">
        <label htmlFor="status">Status</label>
        <select
          id="status"
          value={status}
          onChange={(e) => setStatus(e.target.value)}
        >
          <option value="milik">Dimiliki</option>
          <option value="baca">Sedang Dibaca</option>
          <option value="beli">Akan Dibeli</option>
        </select>
      </div>

      <div className="form-actions">
        <button type="button" className="btn-secondary" onClick={onFormSubmit}>
          Batal
        </button>
        <button type="submit" className="btn-primary">
          {bookToEdit ? "Update" : "Simpan"}
        </button>
      </div>
    </form>
  );
}

export default BookForm;
