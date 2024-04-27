class Observacao:
    id_observacao: str
    id_lembrete: str
    texto: str
    
    def __init__(self, id_observacao: str, id_lembrete: str, texto: str, observacao: dict = None):
        if observacao:
            self.id_observacao = observacao.id_observacao
            self.id_lembrete = observacao.id_lembrete
            self.texto = observacao.texto
        else:
            self.id_observacao = id_observacao
            self.id_lembrete = id_lembrete
            self.texto = texto

    def __str__(self):
        return f'{self.id_lembrete} - {self.id_observacao} - {self.texto}'

    def to_dict(self):
        return {
            "id_observacao": self.id_observacao,
            "id_lembrete": self.id_lembrete,
            "texto": self.texto
        }