import React from "react";
import "./OffersSection.css";

function OffersSection() {
  const offers = [
    {
      id: 1,
      title: "Ofertas Flash ⚡",
      discount: "50% OFF",
      description: "En productos seleccionados",
      bgColor: "#FFE1E1"
    },
    {
      id: 2,
      title: "Envío Premium 🚚",
      description: "¡GRATIS en compras +$100k!",
      bgColor: "#E1F5FE"
    },
    {
      id: 3,
      title: "Cupón Especial 🎁",
      code: "WELCOME10",
      description: "10% extra en tu primera compra",
      bgColor: "#E8F5E9"
    }
  ];

  return (
    <section id="offers" className="offers-section">
      <div className="offers-header">
        <h2>Ofertas Especiales</h2>
        <p>¡No te pierdas nuestras increíbles promociones!</p>
      </div>
      
      <div className="offers-grid">
        {offers.map(offer => (
          <div 
            key={offer.id} 
            className="offer-card"
            style={{ backgroundColor: offer.bgColor }}
          >
            <h3>{offer.title}</h3>
            {offer.discount && (
              <div className="discount-badge">
                {offer.discount}
              </div>
            )}
            <p className="offer-description">{offer.description}</p>
            {offer.code && (
              <button className="coupon-btn">
                Usar código: {offer.code}
              </button>
            )}
          </div>
        ))}
      </div>
    </section>
  );
}

export default OffersSection;