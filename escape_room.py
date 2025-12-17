import flet as ft
from screeninfo import get_monitors

monitor = get_monitors()[0]
WIDTH = monitor.width
HEIGHT = monitor.height

def crea_collegamento(path, testo, collegamenti):
    collegamenti.controls.append(ft.Column([
        ft.Image(src=path, width=100, height=100), 
        ft.Text(testo, size=15, color="white", weight=ft.FontWeight.BOLD)], 
        horizontal_alignment=ft.CrossAxisAlignment.CENTER))

def aggiungi_a_barra_applicazioni(path, row_applicazioni):
    row_applicazioni.controls.append(ft.Image(src=path, width=30, height=30))

def main(page: ft.Page):
    #controlla i tasti per mettere il fullscreen
    def on_key(e: ft.KeyboardEvent): 
        if e.key == "F11":
            page.window.full_screen = not page.window.full_screen 
            page.update()
    page.on_keyboard_event = on_key

    #inizializza schermo
    page.title = "Escape Room"
    page.window.width = WIDTH
    page.window.height = HEIGHT
    page.padding = 0
    page.spacing = 0
    page.bgcolor = ft.Colors.TRANSPARENT
    page.decoration = ft.BoxDecoration(image=ft.DecorationImage(src="img/sfondo_escape_room.jpg", fit=ft.ImageFit.COVER)) #imposta lo sfondo

    #desktop
    collegamenti = ft.Row([], wrap=True, spacing=10, run_spacing=10)
    crea_collegamento("img/cartella.png", "Cartella", collegamenti)
    crea_collegamento("img/file_txt.png", "File1", collegamenti)

    #barra applicazioni
    row_applicazioni = ft.Row(
        controls=[],
        alignment=ft.MainAxisAlignment.START,
        wrap=True,
        spacing=10,
        run_spacing=10,
    )

    barra_applicazioni = ft.Row([
        ft.Container(
        content=row_applicazioni,
        bgcolor=ft.Colors.WHITE,
        width=WIDTH,
        height=50,
        padding=10
    )])

    aggiungi_a_barra_applicazioni("img/logo_windows.png", row_applicazioni)

    #messa a schermo
    page.add(
        ft.Column([collegamenti], expand=True, alignment=ft.MainAxisAlignment.START),

        ft.Column([barra_applicazioni], expand=True, alignment=ft.MainAxisAlignment.END)
    )

ft.app(main)