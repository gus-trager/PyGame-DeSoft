import pygame
import sys
from parametros import WINDOW_HEIGHT, WINDOW_WIDTH, QUIT, lvl3

def tela_transicao2(window):
    tela_transicao = True

    image_tela_transicao2 = pygame.image.load('assets/img/Tela transição 2.png').convert_alpha()
    image_tela_transicao2 = pygame.transform.scale(image_tela_transicao2 , (WINDOW_WIDTH, WINDOW_HEIGHT)).convert_alpha()

    window.fill((0, 0 ,0)) #Preenche a tela com a cor preta
    window.blit(image_tela_transicao2, (0,0))

    pygame.display.update()

    while tela_transicao:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT or (evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE):
                lvl = QUIT
                tela_transicao = False
                #sys.exit()

            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_e:
                tela_transicao = False
                lvl = lvl3

    
    

    return lvl