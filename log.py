import logging
import os

# Ensure the logs directory exists
os.makedirs("logs", exist_ok=True)

# Configure logging
logging.basicConfig(
    filename="logs/valkyrie.log",
    filemode="a",
    format="%(asctime)s | %(levelname)s | %(message)s",
    level=logging.INFO
)

# Console logging during development
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(levelname)s | %(message)s')
console.setFormatter(formatter)

logger = logging.getLogger("Valkyrie")
logger.addHandler(console)