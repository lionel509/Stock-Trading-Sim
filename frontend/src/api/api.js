import axios from 'axios';
const BASE = process.env.REACT_APP_API_URL || 'http://localhost:8000';

export async function getCandles(symbol, interval) {
  const res = await axios.post(`${BASE}/candles`, { symbol, interval });
  return res.data;
}

export async function startSimulation() {
  const res = await axios.post(`${BASE}/simulate`);
  return res.data;
}

export async function placeOrder(order) {
  const res = await axios.post(`${BASE}/order`, order);
  return res.data;
}