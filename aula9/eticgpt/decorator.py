import logging
from typing import Callable

def log(func: Callable):
    
    def wrapper(*args,**kwargs):
    
        logging.info(f"{func.__name__} called")
        result = func(*args,**kwargs)
        return result