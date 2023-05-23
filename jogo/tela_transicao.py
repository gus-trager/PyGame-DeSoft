import pygame
import sys
from assets import *

def tela_transicao(window):

    assets = load_assets()
    tela_transicao = True
    while tela_transicao:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT or (evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_KP_ENTER:
                tela_transicao = False


    window.blit(assets['image_tela_transicao',(0,0)])