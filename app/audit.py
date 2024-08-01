import logging
from datetime import datetime

logging.basicConfig(filename='audit.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def log_event(event: str):
    logging.info(event)