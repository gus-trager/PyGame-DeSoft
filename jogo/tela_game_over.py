import pygame
import sys
from parametros import WINDOW_HEIGHT, WINDOW_WIDTH, QUIT, lvl1, over

#função da tela de game over
def game_over(window):
    image_tela_game_over = pygame.image.load('assets/img/Tela gameover.png').convert_alpha()
    image_tela_game_over = pygame.transform.scale(image_tela_game_over, (WINDOW_WIDTH, WINDOW_HEIGHT))

    window.fill((0,0,0)) #pinta de preto
    window.blit(image_tela_game_over, (0,0)) #posiciona imagem 

    pygame.display.update()
    
    lvl = over
    while lvl == over:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT or (evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE):
                lvl = QUIT
                sys.exit()

            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_e:
                lvl = lvl1
                
    return lvl