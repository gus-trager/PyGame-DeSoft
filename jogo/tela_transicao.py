import pygame
import sys
from assets import *

def tela_transicao(window):
    assets = load_assets()
    tela_transicao = True

    window.fill((0, 0 ,0)) #Preenche a tela com a cor preta
    window.blit(assets['image_tela_transicao'], (0,0))

    pygame.display.update()

    while tela_transicao:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT or (evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE):
                lvl = quit
                #sys.exit()

            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_e:
                tela_transicao = False
                lvl = lvl2

    
    

    return lvl

