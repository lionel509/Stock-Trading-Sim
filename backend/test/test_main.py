import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_candles():
    response = client.post("/candles", json={"symbol": "AAPL", "interval": "1m"})
    assert response.status_code == 200

def test_order():
    response = client.post("/order", json={"symbol": "AAPL", "side": "buy", "price": 150.0, "quantity": 1})
    assert response.status_code == 200