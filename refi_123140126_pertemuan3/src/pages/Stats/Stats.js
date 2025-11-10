import React from "react";
import { useBookStats } from "../../hooks/useBookStats";
import "./Stats.css";

function Stats() {
  const { total, owned, reading, toBuy } = useBookStats();

  return (
    <div className="stats-page">
      <h2>Statistik Buku Anda</h2>
      <div className="stats-grid">
        <div className="stat-card total">
          <h3>Total Buku</h3>
          <p>{total}</p>
        </div>
        <div className="stat-card owned">
          <h3>Dimiliki</h3>
          <p>{owned}</p>
        </div>
        <div className="stat-card reading">
          <h3>Sedang Dibaca</h3>
          <p>{reading}</p>
        </div>
        <div className="stat-card tobuy">
          <h3>Akan Dibeli</h3>
          <p>{toBuy}</p>
        </div>
      </div>
    </div>
  );
}

export default Stats;
