import pygame
import sys
from parametros import WINDOW_HEIGHT, WINDOW_WIDTH, QUIT, lvl2

#função da tela de transição
def tela_transicao1(window):
    image_tela_transicao1 = pygame.image.load('assets/img/Tela transição 1.png').convert_alpha() 
    image_tela_transicao1 = pygame.transform.scale(image_tela_transicao1 , (WINDOW_WIDTH, WINDOW_HEIGHT)).convert_alpha()

    tela_transicao = True

    window.fill((0, 0 ,0)) #Preenche a tela com a cor preta
    window.blit(image_tela_transicao1 , (0,0)) #poscição da imagem de transição

    pygame.display.update()

    while tela_transicao:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT or (evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE):
                lvl = QUIT
                tela_transicao = False
                #sys.exit()

            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_e:
                tela_transicao = False
                lvl = lvl2

    
    

    return lvl

