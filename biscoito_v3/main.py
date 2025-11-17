import flet as ft
from dados import FRASES
from models.biscoito_model import BiscoitoModel

def main(page: ft.Page):
    page.title = "Biscoito da Sorte"
    page.window_width = 500
    page.window_height = 400
    page.window_resizable = False
    page.padding = 30
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    model = BiscoitoModel(FRASES)

    titulo = ft.Text(
        "Biscoito da Sorte",
        size=32,
        weight=ft.FontWeight.BOLD,
        color="amber800",
        text_align=ft.TextAlign.CENTER)

    frase_do_texto = ft.Text(
        "Clique no botão para abrir seu biscoito!",
        size=18,
        text_align=ft.TextAlign.CENTER)

    contador_de_texto = ft.Text(
        "Biscoitos abertos: 0",
        size=14,
        color="grey600",
        text_align=ft.TextAlign.CENTER)

    def abrir_biscoito(e):
        frase = model.obter_frase()
        frase_texto.value = frase
        contador_texto.value = f"Biscoitos abertos: {model.get_total_frases()}"
        page.update()

    def limpar_historico(e):
        model.resetar_historico()
        frase_texto.value = "Clique no botão para abrir seu biscoito!"
        contador_texto.value = "Biscoitos abertos: 0"
        page.update()

    #botões da aplicação
    botao_de_abrir = ft.ElevatedButton(
        "Abrir Biscoito 🥠",
        on_click=abrir_biscoito,
        bgcolor="amber600",
        color="white",
        width=200,
        height=50)

    botao_de_limpar = ft.ElevatedButton(
        "Limpar Histórico",
        on_click=limpar_historico,
        bgcolor="red400",
        color="white",
        width=200,
        height=50)

    page.add(
        ft.Column([
                titulo,
                ft.Container(height=30), 
                frase_do_texto,
                ft.Container(height=30), 
                botao_de_abrir,
                ft.Container(height=10),
                botao_de_limpar,
                ft.Container(height=20),
                contador_de_texto,],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER))

if __name__ == "__main__":
    ft.app(target=main)
