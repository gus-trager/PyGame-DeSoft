import pygame
from parametros import WINDOW_WIDTH, WINDOW_HEIGHT, lvl1, lvl2, lvl3, inicio, inter1, inter2, over, win, QUIT
from tela_inicio import tela_inicio
from tela_transicao1 import tela_transicao1
from tela_transicao2 import tela_transicao2
from tela_fase_1 import fase_lvl1
from tela_fase_2 import fase_lvl2
from tela_fase_3 import fase_lvl3
from tela_game_over import game_over
from tela_vencedor import vencedor
import time


#Inicia Pygame e tela + nome da aba
pygame.init() #Inicialização da biblioteca pygame
pygame.mixer.init() #Inicialização dos audios da biblioteca pygame

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) #Inicial a tela
pygame.display.set_caption("Calvos-Strike") #Nome da aba

#--------------/------------------------/------------------------------/----------------------/----------------------------/---------------/
# Oculta o cursor do mouse
pygame.mouse.set_visible(False)

tempo_inicial = time.time()

lvl = inicio
while lvl != QUIT:
    if lvl == inicio:
        lvl = tela_inicio(window)
    if lvl == lvl1:
        tempo_inicial = time.time()
        lvl = fase_lvl1(window,tempo_inicial)     
    if lvl == inter1:
        lvl = tela_transicao1(window)
    if lvl == inter2:
        lvl = tela_transicao2(window)
    if lvl == lvl2:
        tempo_inicial = time.time()
        lvl = fase_lvl2(window,tempo_inicial)
    if lvl == lvl3:
        tempo_inicial = time.time()
        lvl = fase_lvl3(window,tempo_inicial)
    if lvl == over:
        lvl = game_over(window)
    if lvl == win:
        lvl = vencedor(window)

    

pygame.quit()
