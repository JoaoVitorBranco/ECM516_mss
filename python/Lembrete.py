class Lembrete:
    id_lembrete: str
    texto: str
    
    def __init__(self, id_lembrete: str, texto: str, lembrete: dict = None):
        if lembrete:
            self.id_lembrete = lembrete.id_lembrete
            self.texto = lembrete.texto
        else:
            self.id_lembrete = id_lembrete
            self.texto = texto

    def __str__(self):
        return f'{self.titulo} - {self.descricao}'
    
    def to_dict(self):
        return {
            "id_lembrete": self.id_lembrete,
            "texto": self.texto
        }