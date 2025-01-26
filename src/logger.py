import os
import logging
from datetime import datetime

# Create the directory for logs if it doesn't exist
LOG_DIR = os.path.join(os.getcwd(), "logs")
os.makedirs(LOG_DIR, exist_ok=True)

# Define the log file path
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)

# Set up logging configuration
logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format='[ %(asctime)s ] %(lineno)d - %(name)s - %(levelname)s - %(message)s'
)

