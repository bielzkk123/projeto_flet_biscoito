import flet as ft
from dados import FRASES
from models.biscoito_model import BiscoitoModel
from controllers.biscoito_controller import BiscoitoController
from views.biscoito_view import BiscoitoView

def main(page: ft.Page):
    page.title = "Biscoito da Sorte"
    page.window_width = 500
    page.window_height = 500
    page.window_resizable = False
    page.padding = 30
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    model = BiscoitoModel(FRASES)
    controller = BiscoitoController(model)
    view = BiscoitoView(page, controller)
    controller.view = view  
    view.construir()

if __name__ == "__main__":
    ft.app(target=main)
