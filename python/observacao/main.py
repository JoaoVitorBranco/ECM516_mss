# Import libraries
from fastapi import FastAPI, HTTPException, status
from dotenv import load_dotenv
import os
import uuid
import requests

# Fix import path
import sys
import pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))

# Import packages
from lembrete.DBLembretes import DBLembretes
from lembrete.Lembrete import Lembrete
from DBObservacoes import DBObservacoes
from Observacao import Observacao
from barramento.Evento import Evento

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
    
    
    return dbObservacoes.get_by_lembrete(id_lembrete=id_lembrete)

@app.post("/lembrete/{id_lembrete}/observacao/", status_code=status.HTTP_201_CREATED)
def create_observacao(id_lembrete: str, req: dict):
    
    uuid1 = str(uuid.uuid4())
    observacao = dbObservacoes.put(observacao=Observacao(id_observacao=uuid1, id_lembrete=id_lembrete, texto=req["texto"]))
    
    requests.post("http://localhost:10000/evento", json={
        "tipo": "OBSERVACAO_CREATE",
        "conteudo": observacao.to_dict(),
    })

    return {
        "message": "Item created successfully", 
        "observacao": observacao
    }

# Routes
@app.post("/evento/")
def evento_handler(req: dict):
    evento = Evento(req)
    if evento.tipo == "LEMBRETE_CREATE":

        lembrete = Lembrete(lembrete=evento.conteudo)
        retorno = dbLembretes.put(lembrete=lembrete)
        return {
            "message": "Lembrete criado com sucesso!",
            "lembrete": retorno.to_dict()
        }


# Main
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=PORT)