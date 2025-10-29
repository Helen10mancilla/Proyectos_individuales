import express from "express";
import cors from "cors";
import productosRoutes from "./routes/productos.js";

const app = express();
app.use(cors());
app.use(express.json());

// ✅ Rutas simuladas
app.use("/api/productos", productosRoutes);

// ✅ Servidor
const PORT = 5000;
app.listen(PORT, () => {
  console.log(`🚀 Servidor backend (sin DB) corriendo en http://localhost:${PORT}`);
});

