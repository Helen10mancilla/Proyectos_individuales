import React, { useState } from "react";
import Navbar from "./components/Navbar";
import HeroSection from "./components/HeroSection";
import ProductList from "./components/ProductList";
import Cart from "./components/Cart";
import Footer from "./components/Footer";
import OffersSection from "./components/OffersSection";
import "./App.css";

function App() {
  const [cartVisible, setCartVisible] = useState(false);
  const [cartItems, setCartItems] = useState([]);

  const toggleCart = () => setCartVisible(!cartVisible);

  const addToCart = (product) => setCartItems([...cartItems, product]);

  // 💡 Función para limpiar el carrito (cuando se realiza pedido)
  const clearCart = () => setCartItems([]);

  return (
    <div className="app-container">
      <Navbar toggleCart={toggleCart} cartCount={cartItems.length} />
      <HeroSection />
      <OffersSection /> 
      <div className="content">
        <ProductList addToCart={addToCart} />
        <Footer />
      </div>

      {/* 🛒 Carrito flotante, visible solo cuando cartVisible es true */}
      {cartVisible && (
        <Cart
          visible={cartVisible}
          cartItems={cartItems}
          onClose={toggleCart}
          clearCart={clearCart}
          setCartItems={setCartItems}
        />
      )}
    </div>
  );
}


export default App;
