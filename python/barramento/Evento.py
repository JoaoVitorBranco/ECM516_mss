class Evento:
    tipo: str
    conteudo: dict
    
    def __init__(self, body: dict):
        self.tipo = body.get("tipo")
        self.conteudo = body.get("conteudo")

    def __str__(self):
        return f'{self.tipo} : {self.conteudo}'
    
    def to_dict(self):
        return {
            "tipo": self.tipo,
            "conteudo": self.conteudo
        }