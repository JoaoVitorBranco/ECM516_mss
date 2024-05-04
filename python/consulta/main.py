# Import libraries
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
from DBConsulta import DBConsulta
import os

# Fix import path
import sys
import pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))

# Import packages
from barramento.Evento import Evento
from lembrete.Lembrete import Lembrete
from observacao.Observacao import Observacao

# Variables
app = FastAPI()
db_consulta = DBConsulta()

# Load .env variables
load_dotenv()

# Load environment variables
if os.getenv("PORT"):
    PORT = int(os.getenv("PORT"))

# Routes
@app.get("/lembretes/")
def get_lembretes():
    return db_consulta.get_all_lembretes()

@app.post("/evento/")
def evento_handler(req: dict):
    evento = Evento(req)
    if evento.tipo == "LEMBRETE_CREATE":
        lembrete = Lembrete(lembrete=evento.conteudo)
        retorno = db_consulta.create_lembrete(lembrete=lembrete)
        return {
            "message": "Lembrete criado com sucesso!",
            "lembrete": retorno.to_dict()
        }
    
    if evento.tipo == "OBSERVACAO_CREATE":
        observacao = Observacao(observacao=evento.conteudo)
        retorno = db_consulta.create_observacao(observacao=observacao)
        return {
            "message": "Observação criada com sucesso!",
            "observacao": retorno.to_dict()
        }

# Main
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=PORT)