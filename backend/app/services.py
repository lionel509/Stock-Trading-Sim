import yfinance as yf
import logging
from .gemma_client import GemmaClient
from .schemas import OrderRequest

gemma = GemmaClient("http://gemma3:8001")

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def get_candles(symbol: str, interval: str):
    logger.info(f"Fetching candles for symbol: {symbol}, interval: {interval}")
    data = yf.download(tickers=symbol, period="1d", interval=interval)
    result = data.reset_index().to_dict(orient="records")
    logger.info(f"Fetched candles: {result}")
    return result

async def place_order(order: OrderRequest):
    logger.info(f"Placing order: {order.dict()}")
    # TODO: implement simulated order logic
    result = {"status": "success", "order": order.dict()}
    logger.info(f"Order result: {result}")
    return result

async def start_simulation():
    logger.info("Starting simulation")
    # TODO: orchestrate simulation loop with predictions
    result = {"profit": 0, "trades": []}
    logger.info(f"Simulation result: {result}")
    return result