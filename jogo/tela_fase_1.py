import pygame
import sys
from assets import *
from parametros import *


def fase_lvl1(window,tempo_inicial):

    clock = pygame.time.Clock()

    assets = load_assets()

    assets['som_ambiente1'].play()

    all_passaros = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()

    #Criando vários passasor
    for i in range(10):
        passaro = Passaro1([assets['image_passaro1'], assets['image_passaro1_in']])
        all_passaros.add(passaro)
        all_sprites.add(passaro)


    tempo_restante = 30
    pontos = 0
    
    lvl = lvl1

    while lvl == lvl1:
        clock.tick(FPS)

        

        #Eventos
        eventos = pygame.event.get() #Variavel para acessar os eventos do teclado/mouse
        for evento in eventos:
            if evento.type == pygame.QUIT or (evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE):
                lvl = QUIT #Fecha o pygame
                sys.exit() #Sai pela rotina do sistema
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == pygame.BUTTON_LEFT:
                assets['som_arma1'].play()
                posicao = (ponta_arma_x_lvl_1, ponta_arma_y_lvl_1)  # Escolha a posição desejada
                ponta_arma_img = Ponta_arma(posicao, assets)
                all_sprites.add(ponta_arma_img)
                for passaro in all_passaros:
                    if passaro.rect.collidepoint(evento.pos):
                        passaro.kill()
                        pontos +=100
                        assets['som_score'].play()
                        
                        explosao = Explosao(passaro.rect.center, assets)
                        all_sprites.add(explosao)
        
        #Atualiza a posição dos pássaros
        all_sprites.update()



        #Atualiza a mira
        mouse_pos = pygame.mouse.get_pos()
        assets['mira_rect'].center = mouse_pos


        #Atualiza o relogio
        if tempo_restante > 0:
            tempo_atual = time.time() - tempo_inicial
            tempo_restante = tempo_total - int(tempo_atual)
        else:
            tempo_restante = 0




        window.fill((0, 0 ,0)) #Preenche a tela com a cor preta
        window.blit(assets['image_backgroud_1'], (0,0)) #Depois preenche com o backgroud

        #Desenha os passaros na tela
        all_sprites.draw(window)


        #Desenha a mira e a arma na tela
        window.blit(assets['image_mira'], assets['mira_rect'])
        window.blit(assets['image_arma1'], assets['arma1_rect'])

        #Desenha o placar de pontos
        texto_pontos = assets['font'].render("Pontos: " + str(pontos), True, assets['BRANCO'])
        posicao_pontos = texto_pontos.get_rect(bottomright=(WINDOW_WIDTH - 10, WINDOW_HEIGHT - 10))
        window.blit(texto_pontos, posicao_pontos)

        #Desenha o relogio de tempo
        texto_tempo = assets['font'].render("Tempo: " + str(tempo_restante), True, assets['BRANCO'])
        posicao_tempo = texto_tempo.get_rect(bottomright=(WINDOW_WIDTH -10, 40 ))
        window.blit(texto_tempo, posicao_tempo)


        if pontos == pontuacao_max_1:
            pontos = ponta_arma_x_lvl_1
            lvl = inter1
            pygame.mixer.stop()
        if tempo_restante == 0:
            lvl = over
            pygame.mixer.stop()


        pygame.display.update()

    return lvl

