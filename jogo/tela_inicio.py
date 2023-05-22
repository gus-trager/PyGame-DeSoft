import pygame
import sys
from assets import *

#Função da tela de inicio
def tela_inicio(window):

    assets = load_assets()
    tela_inicio = True

    window.fill(assets['PRETO'])
    window.blit(assets['image_tela_inicio'], (0,0))

    fonte_tt = pygame.font.Font(assets['fonte_titulo'], 80)
    texto_titulo = fonte_tt.render("Calvos-Strike", True, assets['VERMELHO'])
    texto_titulo_rect = texto_titulo.get_rect(center=(WINDOW_WIDTH//1.37, WINDOW_HEIGHT //6))

    fonte_i = pygame.font.Font(assets['fonte_instrucoes'], 48)
    texto_intrucoes = fonte_i.render("Pressione qualquer tecla para jogar", True, assets['VERMELHO'])
    texto_intrucoes_rect = texto_intrucoes.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT //1.1))

    window.blit(texto_titulo, texto_titulo_rect)
    window.blit(texto_intrucoes, texto_intrucoes_rect)

    window.blit(assets['image_sapiro'], (WINDOW_WIDTH//1.8, WINDOW_HEIGHT //3.5))
    window.blit(assets['image_zorzi'], (WINDOW_WIDTH//1.47, WINDOW_HEIGHT //3.5))
    window.blit(assets['image_gus'], (WINDOW_WIDTH//1.25, WINDOW_HEIGHT //3.5))
    pygame.display.update()


    while tela_inicio:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT or (evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:
                tela_inicio = False