import pygame
from classes import *
from assets import *
from parametros import *
from tela_inicio import *
from tela_transicao1 import *
from tela_transicao2 import *
from tela_fase_1 import *
from tela_fase_2 import *
from tela_fase_3 import *
from tela_game_over import *
from tela_vencedor import *


#Inicia Pygame e tela + nome da aba
pygame.init() #Inicialização da biblioteca pygame
pygame.mixer.init() #Inicialização dos audios da biblioteca pygame

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) #Inicial a tela
pygame.display.set_caption("Calvos-Strike") #Nome da aba

#--------------/------------------------/------------------------------/----------------------/----------------------------/---------------/
# Oculta o cursor do mouse
pygame.mouse.set_visible(False)
assets = load_assets()


lvl = inicio
while lvl != quit:
    if lvl == inicio:
        lvl = tela_inicio(window)
    if lvl == lvl1:
        lvl = fase_lvl1(window)
    if lvl == inter1:
        lvl = tela_transicao1(window)
    if lvl == inter2:
        lvl = tela_transicao2(window)
    if lvl == lvl2:
        lvl = fase_lvl2(window)
    if lvl == lvl3:
        lvl = fase_lvl3(window)
    if lvl == over:
        lvl = game_over(window)
    if lvl == win:
        lvl = vencedor(window)

    

pygame.quit()
