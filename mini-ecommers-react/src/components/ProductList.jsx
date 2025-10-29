import React from "react";
import "./ProductList.css";

const products = [
  {
    id: 1,
    name: "Camiseta Premium",
    price: 50000,
    image: "src/assets/img/camisa premiun.jpg",
    category: "Ropa",
    rating: 4.5,
    stock: 10
  },
  {
    id: 2,
    name: "Sudadera Oversize",
    price: 95000,
    image: "src/assets/img/sudadera.jpg",
    category: "Ropa",
    rating: 4.8,
    stock: 5
  },
  {
    id: 3,
    name: "Gorra Casual",
    price: 35000,
    image: "src/assets/img/gorra casual.jpg",
    category: "Accesorios",
    rating: 4.2,
    stock: 15
  },
  {
    id: 4,
    name: "Tenis Urbanos",
    price: 180000,
    image: "src/assets/img/tennis urbanos.jpg",
    category: "Calzado",
    rating: 4.9,
    stock: 8
  }
];

function ProductList({ addToCart }) {
  const renderStars = (rating) => {
    return "★".repeat(Math.floor(rating)) + "☆".repeat(5 - Math.floor(rating));
  };

  return (
    <section className="products-section">
      <div className="products-header">
        <h2>Nuestros Productos</h2>
        <p>Descubre nuestra selección exclusiva</p>
      </div>

      <div className="product-grid">
        {products.map((product) => (
          <div className="product-card" key={product.id}>
            <div className="product-image-container">
              <img src={product.image} alt={product.name} />
              <div className="product-category">{product.category}</div>
            </div>
            
            <div className="product-info">
              <h3>{product.name}</h3>
              <div className="product-rating">
                <span className="stars">{renderStars(product.rating)}</span>
                <span className="rating-number">({product.rating})</span>
              </div>
              <div className="product-price">
                ${product.price.toLocaleString()}
              </div>
              <div className="stock-info">
                Stock disponible: {product.stock} unidades
              </div>
              <button 
                className="add-to-cart-btn"
                onClick={() => addToCart(product)}
              >
                Agregar al carrito 🛍️
              </button>
            </div>
          </div>
        ))}
      </div>
    </section>
  );
}

export default ProductList;



