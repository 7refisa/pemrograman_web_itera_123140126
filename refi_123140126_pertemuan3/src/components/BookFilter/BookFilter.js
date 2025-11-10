import React from "react";
import "./BookFilter.css";

function BookFilter({
  searchTerm,
  setSearchTerm,
  filterStatus,
  setFilterStatus,
}) {
  return (
    <div className="filter-container">
      <div className="filter-group search-group">
        <label htmlFor="search">Cari Buku</label>
        <input
          type="search"
          id="search"
          placeholder="Cari berdasarkan judul atau penulis..."
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
        />
      </div>
      <div className="filter-group status-group">
        <label>Filter Status</label>
        <div className="radio-buttons">
          <button
            className={`radio-btn ${filterStatus === "semua" ? "active" : ""}`}
            onClick={() => setFilterStatus("semua")}
          >
            Semua
          </button>
          <button
            className={`radio-btn ${filterStatus === "milik" ? "active" : ""}`}
            onClick={() => setFilterStatus("milik")}
          >
            Dimiliki
          </button>
          <button
            className={`radio-btn ${filterStatus === "baca" ? "active" : ""}`}
            onClick={() => setFilterStatus("baca")}
          >
            Dibaca
          </button>
          <button
            className={`radio-btn ${filterStatus === "beli" ? "active" : ""}`}
            onClick={() => setFilterStatus("beli")}
          >
            Akan Dibeli
          </button>
        </div>
      </div>
    </div>
  );
}

export default BookFilter;
