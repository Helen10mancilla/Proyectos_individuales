// src/api.js
const API_URL = "http://localhost:5000/api";

export async function getProductos() {
  const response = await fetch(`${API_URL}/productos`);
  const data = await response.json();
  return data;
  
}
