import flet as ft

class BiscoitoView:
    def __init__(self, page, controller):
        self.page = page
        self.controller = controller

        self.titulo = ft.Text(
            "Biscoito da Sorte",
            size=32,
            weight=ft.FontWeight.BOLD,
            color="amber800",
            text_align=ft.TextAlign.CENTER)

        self.frase_texto = ft.Text(
            "Clique no botão para abrir o biscoito!",
            size=18,
            text_align=ft.TextAlign.CENTER)

        self.contador_texto = ft.Text(
            "Biscoitos a serem abertos: 0",
            size=14,
            color="grey600",
            text_align=ft.TextAlign.CENTER)

        self.historico_titulo = ft.Text(
            "Histórico:",
            size=16,
            weight=ft.FontWeight.BOLD,
            color="bluegrey700")

        self.historico_lista = ft.Text(
            "",
            size=14,
            color="white")

    def construir(self):
        botao_abrir = ft.ElevatedButton(
            "Abrir Biscoito",
            on_click=lambda e: self.controller.abrir_biscoito(),
            bgcolor="amber600",
            color="white",
            width=200,
            height=50,)

        botao_limpar = ft.ElevatedButton(
            "Limpar Histórico",
            on_click=lambda e: self.controller.resetar(),
            bgcolor="red400",
            color="white",
            width=200,
            height=50,)

        self.page.add(
            ft.Column([
                    self.titulo,
                    ft.Container(height=20),
                    self.frase_texto,
                    ft.Container(height=20),
                    botao_abrir,
                    ft.Container(height=10),
                    botao_limpar,
                    ft.Container(height=20),
                    self.contador_texto,
                    ft.Container(height=10),
                    self.historico_titulo,
                    self.historico_lista,],
                    alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER,))

    def atualizar_frase(self, frase, total, historico):
        self.frase_texto.value = frase
        self.contador_texto.value = f"Biscoitos abertos: {total}"
        self.historico_lista.value = "\n".join(historico)
        self.page.update()

    def reiniciar(self):
        self.frase_texto.value = "Clique no botão para abrir o biscoito!"
        self.contador_texto.value = "Biscoitos a serem abertos: 0"
        self.historico_lista.value = " "
        self.page.update()
