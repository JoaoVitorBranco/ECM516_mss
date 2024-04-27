from typing import Dict
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
import os
import uuid

from DBLembretes import DBLembretes
from DBObservacoes import DBObservacoes
from Observacao import Observacao

# Variables
app = FastAPI()
dbObservacoes = DBObservacoes()
dbLembretes = DBLembretes()

# Load .env variables
load_dotenv()

# Load environment variables
if os.getenv("PORT"):
    PORT = int(os.getenv("PORT"))

# Routes
@app.get("/lembrete/{id_lembrete}/observacao/")
def get_observacao(id_lembrete: str):
    
    lembrete = dbLembretes.get(id_lembrete=id_lembrete)
    if not lembrete:
        raise HTTPException(status_code=404, detail="Item not found")
    
    return dbObservacoes.get_by_lembrete(id_lembrete=id_lembrete)

@app.post("/lembrete/{id_lembrete}/observacao/")
def create_observacao(id_lembrete: str, req: dict):
    
    lembrete = dbLembretes.get(id_lembrete=id_lembrete)
    if not lembrete:
        raise HTTPException(status_code=404, detail="Item not found")
    
    uuid1 = str(uuid.uuid4())
    observacao = dbObservacoes.put(observacao=Observacao(id_observacao=uuid1, id_lembrete=id_lembrete, texto=req["texto"]))
    
    return {
        "message": "Item created successfully", 
        "observacao": observacao
    }

# Main
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=PORT)