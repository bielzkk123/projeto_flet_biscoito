class BiscoitoController:
    def __init__(self, model):
        self.model = model
        self.view = None
 
    def abrir_biscoito(self):
        frase, total_abertos, historico = self.model.obter_frase()
        self.view.atualizar_frase(frase, total_abertos, historico)
 
    def resetar(self):
        self.model.resetar_historico()
        self.view.reiniciar()
