import React from "react";
import "./HeroSection.css";
import shoppingVideo from "../assets/videos/shopping.mp4"; // Añade esta línea

function HeroSection() {
  return (
    <section className="hero">
      <div className="hero-content">
        <div className="hero-text">
          <h1>Descubre tu Estilo</h1>
          <p>Las mejores marcas y tendencias en un solo lugar</p>
          <div className="hero-buttons">
            <button className="primary-btn" onClick={() => document.getElementById('offers').scrollIntoView({ behavior: 'smooth' })}>
              Ver Ofertas
            </button>
            <button className="secondary-btn" onClick={() => document.getElementById('products').scrollIntoView({ behavior: 'smooth' })}>
              Explorar Productos
            </button>
          </div>
          <div className="hero-features">
            <div className="feature">
              <span>🚚</span>
              <p>Envío Gratis</p>
            </div>
            <div className="feature">
              <span>⚡</span>
              <p>Entrega Rápida</p>
            </div>
            <div className="feature">
              <span>💯</span>
              <p>Calidad Garantizada</p>
            </div>
          </div>
        </div>
        <div className="hero-image">
           <video
            className="animated-video"
            autoPlay
            loop
            muted
            playsInline
          >
            <source src={shoppingVideo} type="video/mp4" />
            Tu navegador no soporta videos
          </video>
        </div>
      </div>
    </section>
  );
}

export default HeroSection;