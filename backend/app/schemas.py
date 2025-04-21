from pydantic import BaseModel

class CandleRequest(BaseModel):
    symbol: str
    interval: str

    def log_data(self):
        return self.dict()

class OrderRequest(BaseModel):
    symbol: str
    side: str  # 'buy' or 'sell'
    price: float
    quantity: int

    def log_data(self):
        return self.dict()