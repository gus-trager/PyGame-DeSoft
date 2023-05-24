import pygame
import sys
from assets import *
from parametros import *

def game_over(window):
    assets = load_assets()
    tela_game_over = True

    window.fill(assets['PRETO'])
    window.blit(assets['image_tela_game_over'], (0,0))

    pygame.display.update()
    
    lvl = over
    while lvl == over:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT or (evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE):
                lvl = quit
                sys.exit()

            if evento.type == pygame.KEYDOWN:
                lvl = lvl1
                
                

    return lvl