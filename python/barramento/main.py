# Import libraries
from typing import Dict
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
import os
import requests

# Fix import path
import sys
import pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))

# Variables
app = FastAPI()

# Load .env variables
load_dotenv()

# Load environment variables
if os.getenv("PORT"):
    PORT = int(os.getenv("PORT"))

# Routes
@app.post("/evento/")
def evento_handler(req: dict):
    requests.post("http://localhost:4000/evento", json=req)
    requests.post("http://localhost:5000/evento", json=req)
    return {
        "message": "Eventos disparados com sucesso!"
    }

# Main
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=PORT)