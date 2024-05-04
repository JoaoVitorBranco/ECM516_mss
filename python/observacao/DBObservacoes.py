from typing import List
import uuid
from observacao.Observacao import Observacao

class DBObservacoes:
    table: List[Observacao]

    def __init__(self):
        uuid1 = str(uuid.uuid4())
        uuid2 = str(uuid.uuid4())
        self.table = [
            Observacao(id_observacao=uuid1, id_lembrete="1", texto="Pilão"),
            Observacao(id_observacao=uuid2, id_lembrete="2", texto="Treinar crau"),
        ]

    def get(self, id_observacao: str):
        for observacao in self.table:
            if observacao.id_observacao == id_observacao:
                return observacao
        return None
    
    def get_all(self):
        return self.table
    
    def get_by_lembrete(self, id_lembrete: str):
        return [observacao for observacao in self.table if observacao.id_lembrete == id_lembrete]

    def put(self, observacao: Observacao):
        for i, obs in enumerate(self.table):
            if obs.id_observacao == observacao.id_observacao:
                self.table[i] = observacao
                return observacao
        self.table.append(observacao)
        return observacao
    
    def pop(self, id_lembrete: str):
        for i, observacao in enumerate(self.table):
            if observacao.id_lembrete == id_lembrete:
                return self.table.pop(i)
        return None
    
    def length(self):
        return len(self.table)