# Fix import path
import sys
import pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))

# Import packages
from lembrete.Lembrete import Lembrete
from observacao.Observacao import Observacao
from typing import Dict
import uuid

class DBConsulta:
    table_lembrete: Dict[str, Lembrete]
    table_consulta: Dict[str, Observacao]

    def __init__(self):
        self.table_lembrete = {
            "1": Lembrete(id_lembrete="1", texto="Fazer Café"),
            "2": Lembrete(id_lembrete="2", texto="Natação"),
        }

        uuid1 = str(uuid.uuid4())
        uuid2 = str(uuid.uuid4())

        self.table_consulta = {
            uuid1: Observacao(id_observacao=uuid1, id_lembrete="1", texto="Pilão"),
            uuid2: Observacao(id_observacao=uuid2, id_lembrete="2", texto="Treinar crau"),
        }

    def create_lembrete(self, lembrete: Lembrete):
        if self.table_lembrete.get(lembrete.id_lembrete, False):
            return None
        self.table_lembrete[lembrete.id_lembrete] = lembrete    
        return lembrete

    def create_observacao(self, observacao: Observacao):
        if self.table_consulta.get(observacao.id_observacao, False):
            return None
        self.table_consulta[observacao.id_observacao] = observacao
        return observacao
    
    def get_observacoes_by_lembretes(self, id_lembrete: str):
        retorno = {}
        for k, v in self.table_consulta.items():
            if v.id_lembrete == id_lembrete:
                retorno[k] = v.to_dict()
        return retorno

    def get_all_lembretes(self):
        retorno = {}
        for k, v in self.table_lembrete.items():
            lembrete = v.to_dict()
            lembrete["observacoes"] = self.get_observacoes_by_lembretes(id_lembrete=k)
            retorno[k] = lembrete

        return retorno
    