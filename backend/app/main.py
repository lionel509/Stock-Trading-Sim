from fastapi import FastAPI
import logging
from app.services import start_simulation, get_candles, place_order
from app.schemas import CandleRequest, OrderRequest

app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.post("/candles")
async def candles(req: CandleRequest):
    logger.info(f"Received request for /candles with data: {req}")
    return await get_candles(req.symbol, req.interval)

@app.post("/order")
async def order(req: OrderRequest):
    logger.info(f"Received request for /order with data: {req}")
    return await place_order(req)

@app.post("/simulate")
async def simulate():
    logger.info("Received request for /simulate")
    return await start_simulation()