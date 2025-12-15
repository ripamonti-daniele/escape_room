import pygame
from sys import exit

pygame.init()
WIDTH = 960
HEIGHT = 540
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Escape room cybersecurity")
clock = pygame.time.Clock()

def crea_collegamento(surf, collegamenti):
    if len(collegamenti) == 0:
        collegamenti.append([surf, surf.get_rect(topleft=(10, 10))])
    else:
        if collegamenti[-1][1].right + surf.get_width() + 10 > WIDTH:
            collegamenti.append([surf, surf.get_rect(topleft=(10, collegamenti[-1][1].bottom + 10))])
        else:
            collegamenti.append([surf, surf.get_rect(topleft=(collegamenti[-1][1].right + 10, collegamenti[-1][1].y))])

def aggiungi_a_barra_applicazioni(surf, barra_applicazioni):
    if len(barra_applicazioni) == 0:
        barra_applicazioni.append([surf, surf.get_rect(bottomleft=(10, HEIGHT - 10))])
    else:
        barra_applicazioni.append([surf, surf.get_rect(bottomleft=(barra_applicazioni[-1][1].right + 10, barra_applicazioni[-1][1].bottom))])

#VARIABILI E SPRITE
gioca = True

sfondo_surf = pygame.image.load("img/sfondo_escape_room.jpg").convert()
sfondo_surf = pygame.transform.scale(sfondo_surf, (WIDTH, HEIGHT))

cartella_surf = pygame.image.load("img/cartella.png").convert_alpha()
cartella_surf = pygame.transform.scale(cartella_surf, (100, 100))
filetxt_surf = pygame.image.load("img/file_txt.png").convert_alpha()
filetxt_surf = pygame.transform.scale(filetxt_surf, (100, 100))
logo_windows_surf = pygame.image.load("img/logo_windows.png").convert_alpha()
logo_windows_surf = pygame.transform.scale(logo_windows_surf, (30, 30))

collegamenti = []
crea_collegamento(cartella_surf, collegamenti)
crea_collegamento(filetxt_surf, collegamenti)

barra_applicazioni = []
aggiungi_a_barra_applicazioni(logo_windows_surf, barra_applicazioni)

while gioca:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gioca = False


    screen.blit(sfondo_surf, (0, 0))
    pygame.draw.rect(screen, (255, 255, 255), (0, HEIGHT - 50, WIDTH, 50))
    for i in barra_applicazioni:
        screen.blit(i[0], i[1])

    for i in collegamenti:
        screen.blit(i[0], i[1])

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
exit()