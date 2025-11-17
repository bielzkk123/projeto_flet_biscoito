import random
 
class BiscoitoModel:
    def __init__(self, frases):
        self.frases = frases
        self.historico = []
        self.frase_anterior = None
 
    def obter_frase(self):
        tentativas = 0
        frase = random.choice(list(self.frases.values()))
        while frase == self.frase_anterior and tentativas < 3:
            frase = random.choice(self.frases)
            tentativas += 1
        self.historico.append(frase)
        self.frase_anterior = frase
        return frase
 
    def resetar_historico(self):
        self.historico.clear()
        self.frase_anterior = None
 
    def obter_total_de_frases(self):
        return len(self.historico)
 
    def obter_historico(self):
        return self.historico.copy()
 
