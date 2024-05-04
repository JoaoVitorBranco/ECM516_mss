from lembrete.Lembrete import Lembrete
from typing import Dict

class DBLembretes:
    table: Dict[str, Lembrete]

    def __init__(self):
        self.table = {
            "1": Lembrete(id_lembrete="1", texto="Fazer Café"),
            "2": Lembrete(id_lembrete="2", texto="Natação"),
        }

    def get(self, id_lembrete: str):
        return self.table.get(id_lembrete, None)
    
    def get_all(self):
        return self.table
    
    def put(self, lembrete: Lembrete):
        self.table[lembrete.id_lembrete] = lembrete
        return lembrete
    
    def pop(self, id_lembrete: str):
        return self.table.pop(id_lembrete, None)
    
    def length(self):
        return len(self.table)