import logging
import time
from typing import List, Optional, Dict, Any
from uuid import UUID
import uvicorn

from fastapi import FastAPI, HTTPException, Depends, Request

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
  uvicorn.run(app, host="127.0.0.1", port=8000)