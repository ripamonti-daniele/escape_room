import flet as ft
from screeninfo import get_monitors
import subprocess
import threading

monitor = get_monitors()[0]
WIDTH = monitor.width / 2
HEIGHT = monitor.height / 2

def main(page: ft.Page):
    #controlla i tasti per mettere il fullscreen
    def on_key(e: ft.KeyboardEvent): 
        if e.key == "F11":
            page.window.full_screen = not page.window.full_screen 
            page.update()
    page.on_keyboard_event = on_key

    # cleanup automatico alla chiusura della finestra
    def clear(e):
        for nome, proc, _ in processi_aperti:
            if proc.poll() is None:   # se è ancora attivo
                proc.terminate()      # chiudi il processo
        print("Tutti i sottoprocessi terminati")

    # page.on_close = clear
    # page.on_disconnect = clear

    #aggiunge collegamento al desktpo
    def crea_collegamento(icona, testo, collegamenti):
        collegamenti.controls.append(
            ft.Container(
            ft.Column([
            icona, 
            ft.Text(testo, size=15, color="white", weight=ft.FontWeight.BOLD)], 
            horizontal_alignment=ft.CrossAxisAlignment.CENTER), 
            on_click=lambda e: apri_scheda(e, icona, row_applicazioni, testo)))
        page.update()

    #aggiunge app alla barra applicazioni
    def aggiungi_a_barra_applicazioni(icona, row_applicazioni):
        container = ft.Container(
            content=icona,
            width=35,
            height=35,
            bgcolor=ft.Colors.with_opacity(0.5, ft.Colors.GREY),
            border=ft.border.all(2, ft.Colors.GREY_500),
            border_radius=ft.border_radius.all(5),
        )
        row_applicazioni.controls.append(container)
        page.update()
        return container


    #funzione del thread che controlla sempre se un'applicazione è stata chiusa e la rimuove
    def pulisci_barra_applicazioni():
        while True:
            for p in processi_aperti[:]:
                if p[1].poll() is not None:  # processo chiuso
                    row_applicazioni.controls.remove(p[2])  # rimuovi il container
                    processi_aperti.remove(p)
                    page.update()


    #apre una nuova scheda se non è già aperta
    def apri_scheda(e, icona, row_applicazioni, nome_processo):
        if not any(p[0] == nome_processo for p in processi_aperti) and nome_processo != "Cestino":
            icona_clone = ft.Icon(name=icona.name, size=30, color=icona.color)
            container = aggiungi_a_barra_applicazioni(icona_clone, row_applicazioni)
            proc = subprocess.Popen(["python", "cartella.py"])
            processi_aperti.append([nome_processo, proc, container])


    processi_aperti = []
    threading.Thread(target=pulisci_barra_applicazioni, daemon=True).start()

    #inizializza schermo
    page.title = "Escape Room"
    page.window.width = WIDTH
    page.window.height = HEIGHT
    page.padding = 0
    page.spacing = 0
    page.bgcolor = ft.Colors.TRANSPARENT
    page.decoration = ft.BoxDecoration(image=ft.DecorationImage(src="img/sfondo_escape_room.jpg", fit=ft.ImageFit.COVER)) #imposta lo sfondo
    # page.window.full_screen = True

    #desktop
    collegamenti = ft.Row([], wrap=True, spacing=10, run_spacing=10)
    crea_collegamento(ft.Icon(name=ft.Icons.RESTORE_FROM_TRASH, size=100, color="grey"), "Cestino", collegamenti)
    crea_collegamento(ft.Icon(name=ft.Icons.SETTINGS, size=100, color="white"), "Impostazioni", collegamenti)
    crea_collegamento(ft.Icon(name=ft.Icons.FOLDER, size=100, color="yellow"), "Cartella", collegamenti)
    crea_collegamento(ft.Icon(name=ft.Icons.INSERT_DRIVE_FILE, size=100), "File1", collegamenti)


    #barra applicazioni
    row_applicazioni = ft.Row(
        controls=[ft.Image(src="img/logo_windows.png", width=35, height=35)],
        alignment=ft.MainAxisAlignment.START,
        wrap=True,
        spacing=10,
        run_spacing=10,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )

    barra_applicazioni = ft.Row([
        ft.Container(
        content=row_applicazioni,
        bgcolor=ft.Colors.WHITE,
        width=WIDTH * 2,
        height=55,
        padding=10,
    )], vertical_alignment=ft.CrossAxisAlignment.CENTER,)

    #messa a schermo
    page.add(
        ft.Column([collegamenti], expand=True, alignment=ft.MainAxisAlignment.START),

        ft.Column([barra_applicazioni], expand=True, alignment=ft.MainAxisAlignment.END)
    )

ft.app(main)