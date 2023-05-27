import pygame
from classes import *


def load_assets():

    AZUL = (0, 0, 255)
    BRANCO = (255, 255, 255)
    PRETO = (0, 0, 0)
    VERDE = (0, 255, 0)
    VERMELHO = (255, 0, 0)
    AMARELO = (255, 255, 0)
    
    assets = {}

    #Cores
    assets['AZUL'] = AZUL
    assets['BRANCO'] = BRANCO
    assets['PRETO'] = PRETO
    assets['VERDE'] = VERDE
    assets['VERMELHO'] = VERMELHO
    assets['AMARELO'] = AMARELO
    #Background tela inicial
    assets['image_tela_inicio'] = pygame.image.load('assets/img/fundo_inicio.jpg').convert()
    #Background lvl1
    assets['image_backgroud_1'] = pygame.image.load('assets/img/fundo 1.jpg').convert()
    #Background lvl2
    assets['image_backgroud_2'] = pygame.image.load('assets/img/fundo 2.jpg').convert()
    #Background lvl3
    assets['image_backgroud_3'] = pygame.image.load('assets/img/fundo 3.jpg').convert()
    #Backgroud tela de transição 1
    assets['image_tela_transicao1'] = pygame.image.load('assets/img/Tela transição 1.png').convert_alpha()
    assets['image_tela_transicao1'] = pygame.transform.scale(assets['image_tela_transicao1'], (WINDOW_WIDTH, WINDOW_HEIGHT)).convert_alpha()
    #Backgroud tela de transição 2
    assets['image_tela_transicao2'] = pygame.image.load('assets/img/Tela transição 2.png').convert_alpha()
    assets['image_tela_transicao2'] = pygame.transform.scale(assets['image_tela_transicao2'], (WINDOW_WIDTH, WINDOW_HEIGHT)).convert_alpha()
    #Backgroud tela game over
    assets['image_tela_game_over'] = pygame.image.load('assets/img/Tela gameover.png').convert_alpha()
    assets['image_tela_game_over'] = pygame.transform.scale(assets['image_tela_game_over'], (WINDOW_WIDTH, WINDOW_HEIGHT))
    #Background tela vencedor
    assets['image_tela_vencedor'] = pygame.image.load('assets/img/Tela ganhador.png')
    assets['image_tela_vencedor'] = pygame.transform.scale(assets['image_tela_vencedor'], (WINDOW_WIDTH, WINDOW_HEIGHT))
    #Sapiro
    assets['image_sapiro'] = pygame.image.load('assets/img/sapiro.jpg')
    assets['image_sapiro'] = pygame.transform.scale(assets['image_sapiro'], (SAPIRO_WIDTH, SAPIRO_HEIGHT)).convert()
    #Zorzi
    assets['image_zorzi'] = pygame.image.load('assets/img/zorzi.jpg')
    assets['image_zorzi'] = pygame.transform.scale(assets['image_zorzi'],(ZORZI_WIDHT, ZORZI_HEIGHT)).convert()
    #Gus
    assets['image_gus'] = pygame.image.load('assets/img/gus.jpg')
    assets['image_gus'] = pygame.transform.scale(assets['image_gus'],(GUS_WIDHT, GUS_HEIGHT)).convert()
    
    #Passaro1
    assets['image_passaro1'] = pygame.image.load("assets/img/passaro 1.png").convert_alpha()
    assets['image_passaro1'] = pygame.transform.scale(assets['image_passaro1'], (PASSARO_WIDTH, PASSARO_HEIGHT)).convert_alpha()
    #Passaro1 invertido
    assets['image_passaro1_in'] = pygame.image.load("assets/img/passaro 1 in.png").convert_alpha()
    assets['image_passaro1_in'] = pygame.transform.scale(assets['image_passaro1_in'], (PASSARO_WIDTH, PASSARO_HEIGHT)).convert_alpha()
    #Passaro2
    assets['image_passaro2'] = pygame.image.load("assets/img/passaro 2.png").convert_alpha()
    assets['image_passaro2'] = pygame.transform.scale(assets['image_passaro2'], (PASSARO_WIDTH, PASSARO_HEIGHT)).convert_alpha()
    #Passaro2 invertido
    assets['image_passaro2_in'] = pygame.image.load("assets/img/passaro 2 in.png").convert_alpha()
    assets['image_passaro2_in'] = pygame.transform.scale(assets['image_passaro2_in'], (PASSARO_WIDTH, PASSARO_HEIGHT)).convert_alpha()
    #Passaro3
    assets['image_passaro3'] = pygame.image.load("assets/img/passaro 3.png").convert_alpha()
    assets['image_passaro3'] = pygame.transform.scale(assets['image_passaro3'], (PASSARO_WIDTH, PASSARO_HEIGHT)).convert_alpha()
    #Passaro3 invertido
    assets['image_passaro3_in'] = pygame.image.load("assets/img/passaro 3 in.png").convert_alpha()
    assets['image_passaro3_in'] = pygame.transform.scale(assets['image_passaro3_in'], (PASSARO_WIDTH, PASSARO_HEIGHT)).convert_alpha()
    #Manga
    assets['image_manga'] = pygame.image.load("assets/img/manga.png")
    assets['image_manga'] = pygame.transform.scale(assets['image_manga'],(PASSARO_WIDTH, PASSARO_HEIGHT)).convert_alpha() 
    
    #Mira
    assets['image_mira'] = pygame.image.load("assets/img/mira.png").convert_alpha()
    assets['image_mira'] = pygame.transform.scale(assets['image_mira'], (MIRA_WIDTH, MIRA_HEIGHT)).convert_alpha()
    assets['mira_rect'] = assets['image_mira'].get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
    #Arma1
    assets['image_arma1'] = pygame.image.load('assets/img/arma1.png').convert_alpha()
    assets['image_arma1'] = pygame.transform.scale(assets['image_arma1'], (ARMA1_WIDTH, ARMA1_HEIGHT))
    assets['arma1_rect'] = assets['image_arma1'].get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 1.25))
    #Arma2
    assets['image_arma2'] = pygame.image.load('assets/img/arma2.png').convert_alpha()
    assets['image_arma2'] = pygame.transform.scale(assets['image_arma2'], (ARMA2_WIDTH, ARMA2_HEIGHT))
    assets['arma2_rect'] = assets['image_arma2'].get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 1.25))
    #Arma3
    assets['image_arma3'] = pygame.image.load('assets/img/arma3.png').convert_alpha()
    assets['image_arma3'] = pygame.transform.scale(assets['image_arma3'], (ARMA3_WIDTH, ARMA3_HEIGHT))
    assets['arma3_rect'] = assets['image_arma3'].get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 1.32))
   
    #Som ambiente1
    assets['som_ambiente1'] = pygame.mixer.Sound('assets/sounds/som ambiente 1.mp3')
    #Som ambiente2
    assets['som_ambiente2'] = pygame.mixer.Sound('assets/sounds/som ambiente 2.mp3')
    #Som ambiente3
    assets['som_ambiente3'] = pygame.mixer.Sound('assets/sounds/som ambiente 3.wav')
    #Som tela de inicio

    #Som arma1
    assets['som_arma1'] = pygame.mixer.Sound('assets/sounds/tiro arma1.mp3')
    #Som arma2
    assets['som_arma2'] = pygame.mixer.Sound('assets/sounds/tiro arma2.mp3')
    #Som arma3
    assets['som_arma3'] = pygame.mixer.Sound('assets/sounds/tiro arma3.mp3')
    #Som score
    assets['som_score'] = pygame.mixer.Sound('assets/sounds/score2.wav')
    #Zé da manga
    assets['ze_da_manga'] = pygame.mixer.Sound('assets/sounds/zé da manga.mp3')


    #Fonte padrão
    assets['font'] = pygame.font.SysFont(None, 48)
    # Fonte do Titulo do jogo
    assets['fonte_titulo'] = 'assets/img/fonte titulo1.ttf'
    # Fonte do Instrucoes do jogo
    assets['fonte_instrucoes'] = 'assets/img/fonte instrucoes.TTF'

    explosion_anim = []
    ponta_arma = []

    for i in range(10):
        filename = 'assets/img/explosao0{}.png'.format(i)
        img = pygame.image.load(filename)
        img = pygame.transform.scale(img, (32, 32))
        explosion_anim.append(img)

    for i in range(2):
        filename = 'assets/img/explosao1{}.png'.format(i)
        img = pygame.image.load(filename)
        img = pygame.transform.scale(img, (32, 32))
        explosion_anim.append(img)

    assets['explosion_anim'] = explosion_anim 

    for i in range(8):
        filename2 = 'assets/img/ponta0{}.png'.format(i)
        img = pygame.image.load(filename2)
        img = pygame.transform.scale(img, (150, 150))
        ponta_arma.append(img)

    assets['ponta_arma'] = ponta_arma

    return assets







#assets['som_ambiente1'].play(-1) #Loop infinito de som ambiente




