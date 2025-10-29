// 📁 src/components/Cart.jsx
import React from "react";
import "./Cart.css";

function Cart({ visible, cartItems, onClose, clearCart, setCartItems }) {
  if (!visible) return null;

  // 🗑️ Función para eliminar un solo producto
  const removeItem = (indexToRemove) => {
    const updatedCart = cartItems.filter((_, index) => index !== indexToRemove);
    setCartItems(updatedCart);
  };

  return (
    <div className="cart-overlay">
      <div className="cart">
        <button className="close-btn" onClick={onClose}>
          ✖
        </button>
        <h2>🛍️ Tu carrito</h2>

        {cartItems.length === 0 ? (
          <p>El carrito está vacío.</p>
        ) : (
          <ul>
            {cartItems.map((item, index) => (
              <li key={index} className="cart-item">
                <span>{item.name}</span>
                <span>${item.price}</span>
                <button
                  className="remove-btn"
                  onClick={() => removeItem(index)}
                >
                  Eliminar
                </button>
              </li>
            ))}
          </ul>
        )}

        {cartItems.length > 0 && (
          <button
            className="checkout-btn"
            onClick={() => {
              alert("✅ Pedido realizado con éxito");
              clearCart(); // Limpia todo el carrito al finalizar pedido
            }}
          >
            Realizar pedido
          </button>
        )}
      </div>
    </div>
  );
}

export default Cart;
