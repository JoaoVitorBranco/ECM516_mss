from typing import Dict
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
import os


from Lembrete import Lembrete
from DB import DB

# Variables
PORT = 8080
app = FastAPI()
db = DB()

# Load .env variables
load_dotenv()

# Load environment variables
if os.getenv("PORT"):
    PORT = int(os.getenv("PORT"))

# Routes
@app.get("/lembrete/")
def get_lembretes():
    return db.get_all()

@app.post("/lembrete/")
def create_item(req: dict):
    idx = str(db.length() + 1)
    lembrete = db.put(lembrete=Lembrete(id_lembrete=idx, texto=req["texto"]))

    return {
        "message": "Item created successfully", 
        "lembrete": lembrete
    }

@app.put("/lembrete/{id_lembrete}")
def update_item(id_lembrete: str, req: Dict[str, str]):
    if id_lembrete not in db.get_all().keys():
        raise HTTPException(status_code=404, detail="Item not found")

    lembrete = db.put(lembrete=Lembrete(id_lembrete=id_lembrete, texto=req["texto"]))
    return {
        "message": "Item updated successfully", 
        "lembrete": lembrete.to_dict()
    }

@app.delete("/lembrete/{id_lembrete}")
def delete_item(id_lembrete: str):
    if id_lembrete not in db.get_all().keys():
        raise HTTPException(status_code=404, detail="Item not found")

    lembrete = db.pop(id_lembrete)
    return {
        "message": "Item deleted successfully", 
        "lembrete": lembrete.to_dict()
    }

# Main
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=PORT)