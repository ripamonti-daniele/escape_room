import flet as ft

def main(page: ft.Page):
    page.title = "Cartella"
    page.bgcolor = ft.Colors.WHITE
    page.window.always_on_top = True

    page.add(
        ft.Column([
            ft.Text("Questa è la scheda della cartella", size=20),
        ], alignment=ft.MainAxisAlignment.CENTER)
    )

ft.app(target=main)
