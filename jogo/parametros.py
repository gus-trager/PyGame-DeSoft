import pygame
import time

# parâmetros janela
WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 900

# parâmetros Sapiro
SAPIRO_WIDTH = 170
SAPIRO_HEIGHT = 170

# parâmetros Zorzi
ZORZI_WIDHT = 170
ZORZI_HEIGHT = 170

# parâmetros Gus
GUS_WIDHT = 170
GUS_HEIGHT = 170

# parâmetros Pássaro
PASSARO_WIDTH = 50
PASSARO_HEIGHT = 50

# parâmetros Mira
MIRA_WIDTH = 70
MIRA_HEIGHT = 70

# parâmetros Arma 1
ARMA1_WIDTH = 400
ARMA1_HEIGHT = 400

# parâmetros Arma 2
ARMA2_WIDTH = 400
ARMA2_HEIGHT = 400

# parâmetros Arma 3
ARMA3_WIDTH = 400
ARMA3_HEIGHT = 400

#Limitador de FPS
FPS = 60

#Valores de tamanho
ponta_arma_x_lvl_1 = 730
ponta_arma_y_lvl_1 = 575

ponta_arma_x_lvl_2 = 690
ponta_arma_y_lvl_2 = 600

ponta_arma_x_lvl_3 = 820
ponta_arma_y_lvl_3 = 730

#Variaveis para serem atualizadas no Game Loop
pontos = 0

tempo_total = 30
tempo_restante = tempo_total
tempo_inicial = time.time() #Retorna o tempo atual durante o loop

pontuacao_max_1 = 1000
pontuacao_max_2 = 1000
pontuacao_max_3 = 1000

#Niveis
inicio = 0
lvl1 = 1
lvl2 = 2
lvl3 = 3
inter1 = 4
inter2 = 5
over = 6
win = 7
quit = 8


