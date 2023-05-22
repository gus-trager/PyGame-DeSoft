import pygame
import sys
import random
import time
from classes import *
from assets import *
from parametros import *
from tela_inicio import *


#Inicia Pygame e tela + nome da aba
pygame.init() #Inicialização da biblioteca pygame
pygame.mixer.init() #Inicialização dos audios da biblioteca pygame
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) #Inicial a tela
pygame.display.set_caption("Calvos-Strike") #Nome da aba

########################################################################## Funções ##############################################################################################
#Função da tela de inicio
def tela_inicio():
    tela_inicio = True

    window.fill(PRETO)
    window.blit(image_tela_inicio, (0,0))

    fonte_tt = pygame.font.Font(fonte_titulo, 80)
    texto_titulo = fonte_tt.render("Calvos-Strike", True, VERMELHO)
    texto_titulo_rect = texto_titulo.get_rect(center=(WINDOW_WIDTH//1.37, WINDOW_HEIGHT //6))

    fonte_i = pygame.font.Font(fonte_instrucoes, 48)
    texto_intrucoes = fonte_i.render("Pressione qualquer tecla para jogar", True, VERMELHO)
    texto_intrucoes_rect = texto_intrucoes.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT //1.1))

    window.blit(texto_titulo, texto_titulo_rect)
    window.blit(texto_intrucoes, texto_intrucoes_rect)

    window.blit(image_sapiro, (WINDOW_WIDTH//1.8, WINDOW_HEIGHT //3.5))
    window.blit(image_zorzi, (WINDOW_WIDTH//1.47, WINDOW_HEIGHT //3.5))
    window.blit(image_gus, (WINDOW_WIDTH//1.25, WINDOW_HEIGHT //3.5))
    pygame.display.update()


    while tela_inicio:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT or (evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:
                tela_inicio = False

tela_inicio()

################################################################################################################################################################################################    
#Game loop
game = True
while game:
    clock.tick(FPS)

    #Eventos
    eventos = pygame.event.get() #Variavel para acessar os eventos do teclado/mouse
    for evento in eventos:
        if evento.type == pygame.QUIT or (evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE):
            game = False #ou pygame.quit()
            sys.exit() #Sai pela rotina do sistema
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == pygame.BUTTON_LEFT:
            som_arma2.play()
            posicao = (ponta_arma_x, ponta_arma_y)  # Escolha a posição desejada
            ponta_arma_img = Ponta_arma(posicao, assets)
            all_passaros.add(ponta_arma_img)
            for passaro in all_passaros:
                if passaro.rect.collidepoint(evento.pos):
                    passaro.kill()
                    pontos +=100
                    som_score.play()
                    
                    explosao = Explosao(passaro.rect.center, assets)
                    all_passaros.add(explosao)
    
    #Atualiza a posição dos pássaros
    all_passaros.update()



    #Atualiza a mira
    mouse_pos = pygame.mouse.get_pos()
    mira_rect.center = mouse_pos


    #Atualiza o relogio
    if tempo_restante > 0:
        tempo_atual = time.time() - tempo_inicial
        tempo_restante = tempo_total - int(tempo_atual)
    else:
        tempo_restante = 0




    window.fill((0, 0 ,0)) #Preenche a tela com a cor preta
    window.blit(image_backgroud, (0,0)) #Depois preenche com o backgroud

    #Desenha os passaros na tela
    all_passaros.draw(window)

   #Desenha a mira e a arma na tela
    window.blit(image_mira, mira_rect)
    window.blit(image_arma2, arma2_rect)

    #Desenha o placar de pontos
    texto_pontos = font.render("Pontos: " + str(pontos), True, BRANCO)
    posicao_pontos = texto_pontos.get_rect(bottomright=(WINDOW_WIDTH - 10, WINDOW_HEIGHT - 10))
    window.blit(texto_pontos, posicao_pontos)

    #Desenha o relogio de tempo
    texto_tempo = font.render("Tempo: " + str(tempo_restante), True, BRANCO)
    posicao_tempo = texto_tempo.get_rect(bottomright=(WINDOW_WIDTH -10, 40 ))
    window.blit(texto_tempo, posicao_tempo)

    pygame.display.update()

pygame.quit()