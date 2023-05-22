import pygame
from parametros import *
from classes import *

#Cores
AZUL = (0, 0, 255)
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)
AMARELO = (255, 255, 0)

#Background tele inicial
image_tela_inicio = pygame.image.load('assets/img/fundo_inicio.jpg').convert()

#Background lvl1
image_backgroud = pygame.image.load('assets/img/fundo 1.jpg').convert()

#Sapiro
image_sapiro = pygame.image.load('assets/img/sapiro.jpg')
image_sapiro = pygame.transform.scale(image_sapiro, (SAPIRO_WIDTH, SAPIRO_HEIGHT)).convert()

#Zorzi
image_zorzi = pygame.image.load('assets/img/zorzi.jpg')
image_zorzi = pygame.transform.scale(image_zorzi,(ZORZI_WIDHT, ZORZI_HEIGHT)).convert()

#Gus
image_gus = pygame.image.load('assets/img/gus.jpg')
image_gus = pygame.transform.scale(image_gus,(GUS_WIDHT, GUS_HEIGHT)).convert()

#Passaro
image_passaro1 = pygame.image.load("assets/img/passaro.png").convert_alpha()
image_passaro1 = pygame.transform.scale(image_passaro1, (PASSARO_WIDTH, PASSARO_HEIGHT)).convert_alpha()

image_passaro2 = pygame.image.load("assets/img/passaro 2.png").convert_alpha()
image_passaro2 = pygame.transform.scale(image_passaro1, (PASSARO_WIDTH, PASSARO_HEIGHT)).convert_alpha()

#Mira 
image_mira = pygame.image.load("assets/img/mira.png").convert_alpha()
image_mira = pygame.transform.scale(image_mira, (MIRA_WIDTH, MIRA_HEIGHT)).convert_alpha()
mira_rect = image_mira.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
# Oculta o cursor do mouse
pygame.mouse.set_visible(False)


#Arma1
image_arma1 = pygame.image.load('assets/img/arma1.png').convert_alpha()
image_arma1 = pygame.transform.scale(image_arma1, (ARMA1_WIDTH, ARMA1_HEIGHT))
arma1_rect = image_arma1.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 1.25))

#Arma2
image_arma2 = pygame.image.load('assets/img/arma2.png').convert_alpha()
image_arma2 = pygame.transform.scale(image_arma2, (ARMA2_WIDTH, ARMA2_HEIGHT))
arma2_rect = image_arma2.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 1.25))

#Arma3
image_arma3 = pygame.image.load('assets/img/arma3.png').convert_alpha()
image_arma3 = pygame.transform.scale(image_arma3, (ARMA3_WIDTH, ARMA3_HEIGHT))
arma3_rect = image_arma3.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 1.32))

#Som ambiente1
som_ambiente1 = pygame.mixer.Sound('assets/sounds/som ambiente 1.mp3')
som_ambiente1.play(-1) #Loop infinito de som ambiente

#Som ambiente2


#Som ambiente3


#Som tela de inicio



#Som arma1
som_arma1 = pygame.mixer.Sound('assets/sounds/tiro arma1.mp3')

#Som arma2
som_arma2 = pygame.mixer.Sound('assets/sounds/tiro arma2.mp3')

#Som arma3
som_arma3 = pygame.mixer.Sound(('assets/sounds/tiro arma3.mp3'))

#Som score
som_score = pygame.mixer.Sound('assets/sounds/score2.wav')


#Fonte tela de inicio

#Fonte padrão
font = pygame.font.SysFont(None, 48)

# Fonte do Titulo do jogo
fonte_titulo = 'assets/img/fonte titulo1.ttf'

# Fonte do Instrucoes do jogo
fonte_instrucoes = 'assets/img/fonte instrucoes.TTF'



assets = {}

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





#Grupo de passaros
all_passaros = pygame.sprite.Group()

#Criando vários passasor
for i in range(10):
    passaro = Passaro(image_passaro1)
    all_passaros.add(passaro)


pygame.display.update()