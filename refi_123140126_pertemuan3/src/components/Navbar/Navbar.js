import React from "react";
import { Link } from "react-router-dom";
import "./Navbar.css";

function Navbar() {
  return (
    <nav className="navbar">
      <h1>✨Manajemen Buku</h1>
      <div className="nav-links">
        <Link to="/">Home</Link>
        <Link to="/stats">Statistik</Link>
      </div>
    </nav>
  );
}

export default Navbar;
