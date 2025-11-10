import React, { createContext, useContext, useState, useEffect } from "react";

const BookContext = createContext();

export function useBooks() {
  return useContext(BookContext);
}

export function BookProvider({ children }) {
  const [books, setBooks] = useState(() => {
    const savedBooks = localStorage.getItem("books");
    return savedBooks ? JSON.parse(savedBooks) : [];
  });

  useEffect(() => {
    localStorage.setItem("books", JSON.stringify(books));
  }, [books]);

  const addBook = (newBook) => {
    setBooks([...books, { ...newBook, id: Date.now().toString() }]);
  };

  const updateBook = (id, updatedBook) => {
    setBooks(
      books.map((book) => (book.id === id ? { ...book, ...updatedBook } : book))
    );
  };

  const deleteBook = (id) => {
    setBooks(books.filter((book) => book.id !== id));
  };

  const value = {
    books,
    addBook,
    updateBook,
    deleteBook,
  };

  return <BookContext.Provider value={value}>{children}</BookContext.Provider>;
}
