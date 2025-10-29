import React from "react";
import "./Navbar.css";

function Navbar({ toggleCart, cartCount }) {
  return (
    <nav className="navbar">
      <div className="nav-content">
        <div className="nav-brand">
          <span className="brand-icon">🛍️</span>
          <h1>El Baúl</h1>
        </div>

        <div className="nav-links">
          <a href="#nav-brand" className="nav-link">Inicio</a>
          <a href="#offers" className="nav-link">Ofertas</a>
          <a href="#product-grid" className="nav-link">Productos</a>
          <button className="cart-button" onClick={toggleCart}>
            <span className="cart-icon">🛒</span>
            {cartCount > 0 && <span className="cart-badge">{cartCount}</span>}
          </button>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;



