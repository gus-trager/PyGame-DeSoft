import pygame
import sys
import time
from classes import *
from assets import *
from parametros import *
from tela_inicio import *
from tela_transicao import *
from tela_fase_1 import *
from tela_fase_2 import *
from tela_fase_3 import *


#Inicia Pygame e tela + nome da aba
pygame.init() #Inicialização da biblioteca pygame
pygame.mixer.init() #Inicialização dos audios da biblioteca pygame

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) #Inicial a tela
pygame.display.set_caption("Calvos-Strike") #Nome da aba

#--------------/------------------------/------------------------------/----------------------/----------------------------/---------------/
# Oculta o cursor do mouse
pygame.mouse.set_visible(False)
assets = load_assets()
fase_lvl3(window)

lvl = inicio
while lvl != quit:
    if lvl == inicio:
        lvl = tela_inicio(window)
    if lvl == lvl1:
        lvl = fase_lvl1(window)
    #if lvl == inter:
        #lvl = tela_transicao(window)
    if lvl == lvl2:
        lvl = fase_lvl2(window)
    if lvl == lvl3:
        lvl = fase_lvl3(window)

pygame.quit()


























































# #Grupo de passaros (TEM QUE IR PARA AS FUNCOES DOS NIVEIS)


# all_passaros = pygame.sprite.Group()

# #Criando vários passasor
# for i in range(10):
#     passaro = Passaro(assets['image_passaro1'])
#     all_passaros.add(passaro)


# #Game loop
# game = True
# while game:
#     clock.tick(FPS)

#     #Eventos
#     eventos = pygame.event.get() #Variavel para acessar os eventos do teclado/mouse
#     for evento in eventos:
#         if evento.type == pygame.QUIT or (evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE):
#             game = False #ou pygame.quit()
#             sys.exit() #Sai pela rotina do sistema
#         if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == pygame.BUTTON_LEFT:
#             assets['som_arma2'].play()
#             posicao = (ponta_arma_x, ponta_arma_y)  # Escolha a posição desejada
#             ponta_arma_img = Ponta_arma(posicao, assets)
#             all_passaros.add(ponta_arma_img)
#             for passaro in all_passaros:
#                 if passaro.rect.collidepoint(evento.pos):
#                     passaro.kill()
#                     pontos +=100
#                     assets['som_score'].play()
                    
#                     explosao = Explosao(passaro.rect.center, assets)
#                     all_passaros.add(explosao)
    
#     #Atualiza a posição dos pássaros
#     all_passaros.update()



#     #Atualiza a mira
#     mouse_pos = pygame.mouse.get_pos()
#     assets['mira_rect'].center = mouse_pos


#     #Atualiza o relogio
#     if tempo_restante > 0:
#         tempo_atual = time.time() - tempo_inicial
#         tempo_restante = tempo_total - int(tempo_atual)
#     else:
#         tempo_restante = 0




#     window.fill((0, 0 ,0)) #Preenche a tela com a cor preta
#     window.blit(assets['image_backgroud1'], (0,0)) #Depois preenche com o backgroud

#     #Desenha os passaros na tela
#     all_passaros.draw(window)

#    #Desenha a mira e a arma na tela
#     window.blit(assets['image_mira'], assets['mira_rect'])
#     window.blit(assets['image_arma2'], assets['arma2_rect'])

#     #Desenha o placar de pontos
#     texto_pontos = assets['font'].render("Pontos: " + str(pontos), True, assets['BRANCO'])
#     posicao_pontos = texto_pontos.get_rect(bottomright=(WINDOW_WIDTH - 10, WINDOW_HEIGHT - 10))
#     window.blit(texto_pontos, posicao_pontos)

#     #Desenha o relogio de tempo
#     texto_tempo = assets['font'].render("Tempo: " + str(tempo_restante), True, assets['BRANCO'])
#     posicao_tempo = texto_tempo.get_rect(bottomright=(WINDOW_WIDTH -10, 40 ))
#     window.blit(texto_tempo, posicao_tempo)

#     pygame.display.update()

# pygame.quit()