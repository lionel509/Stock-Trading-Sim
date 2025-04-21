import httpx
import subprocess
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class GemmaClient:
    def __init__(self, model: str = "gemma3"):
        logger.info(f"Initializing GemmaClient with model '{model}'...")
        print(f"Starting Ollama model '{model}'...")
        # Launch Ollama server
        self.process = subprocess.Popen(["ollama", "serve"])
        time.sleep(5)  # give the server time to initialize
        logger.info("Ollama server is ready.")
        print("Ollama server is ready.")
        # Set up HTTP client to Ollama API
        self.base_url = f"http://localhost:11434/models/{model}"
        self.client = httpx.AsyncClient()

    async def predict(self, data: dict):
        logger.info(f"Sending prediction request with data: {data}")
        response = await self.client.post(self.base_url, json={"prompt": data})
        logger.info(f"Received response: {response.json()}")
        return response.json()