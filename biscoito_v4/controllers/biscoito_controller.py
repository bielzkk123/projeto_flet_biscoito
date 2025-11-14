class BiscoitoController:
    def __init__(self, model):
        self.model = model
        self.view = None  # será associada no main

    def abrir_biscoito(self):
        frase, total, historico = self.model.obter_frase()
        self.view.atualizar_frase(frase, total, historico)

    def resetar(self):
        self.model.resetar_historico()
        self.view.reiniciar()
