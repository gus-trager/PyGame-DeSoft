import pygame
import sys
from parametros import WINDOW_HEIGHT, WINDOW_WIDTH, win, QUIT, lvl1

#função da tela de vencedor
def vencedor(window):
    
    image_tela_vencedor = pygame.image.load('assets/img/Tela ganhador.png')
    image_tela_vencedor = pygame.transform.scale(image_tela_vencedor, (WINDOW_WIDTH, WINDOW_HEIGHT))

    window.fill((0, 0, 0)) #pinta imagem de pret
    window.blit(image_tela_vencedor, (0,0)) #onde a imagem vai estar

    pygame.display.update()

    lvl = win
    while lvl == win:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT or (evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE):
                lvl = QUIT
                pygame.quit()
                #sys.exit()

            
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_e:
                lvl = lvl1

    return lvl