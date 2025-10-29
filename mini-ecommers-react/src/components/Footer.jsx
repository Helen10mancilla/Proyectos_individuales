import React from 'react';
import './Footer.css';

function Footer() {
  return (
    <footer className="footer">
      <div className="footer-content">
        <div className="footer-section">
          <h3>Sobre Nosotros</h3>
          <p>Somos tu tienda de confianza para encontrar las últimas tendencias en moda y accesorios.</p>
          <div className="social-links">
            <a href="#"><i className="fab fa-facebook"></i></a>
            <a href="#"><i className="fab fa-instagram"></i></a>
            <a href="#"><i className="fab fa-twitter"></i></a>
          </div>
        </div>
        
        <div className="footer-section">
          <h3>Enlaces Rápidos</h3>
          <ul>
            <li><a href="#Navbar">Inicio</a></li>
            <li><a href="#product_list">Productos</a></li>
            <li><a href="#offers">Ofertas</a></li>
            <li><a href="#footer">Contacto</a></li>
          </ul>
        </div>
        
        <div className="footer-section">
          <h3>Contacto</h3>
          <ul>
            <li>📍 Dirección: Calle Principal 123</li>
            <li>📞 Teléfono: (123) 456-7890</li>
            <li>✉️ Email: info@tutienda.com</li>
          </ul>
        </div>
        
        <div className="footer-section">
          <h3>Newsletter</h3>
          <p>Suscríbete para recibir las últimas novedades y ofertas especiales.</p>
          <form>
            <input type="email" placeholder="Tu email" />
            <button type="submit">Suscribirse</button>
          </form>
        </div>
      </div>
      
      <div className="footer-bottom">
        <p>&copy; 2025 El baul. Todos los derechos reservados.</p>
      </div>
    </footer>
  );
}

export default Footer;
