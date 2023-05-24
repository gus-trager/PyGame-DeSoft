import pygame
import sys
from assets import *
from parametros import *


def vencedor(window):
    assets = load_assets()
    assets['som_arma3'].stop()

    window.fill((0, 0, 0))
    window.blit(assets['image_tela_vencedor'], (0,0))

    pygame.display.update()

    lvl = win
    while lvl == win:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT or (evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE):
                lvl = quit
                pygame.quit()
                #sys.exit()

            
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_e:
                lvl = lvl1

    return lvl