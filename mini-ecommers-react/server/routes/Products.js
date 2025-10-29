// server/routes/productos.js
import express from "express";
const router = express.Router();

// 🚀 Datos de ejemplo (simulan los que vendrían de MySQL)
const productos = [
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

// ✅ Endpoint que devuelve los productos simulados
router.get("/", (req, res) => {
  res.json(productos);
});

export default router;
