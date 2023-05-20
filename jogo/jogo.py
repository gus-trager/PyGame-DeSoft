import pygame
import sys
import random
import time

#Cores
AZUL = (0, 0, 255)
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)
AMARELO = (255, 255, 0)

#Inicia Pygame e tela + nome da aba
pygame.init() #Inicialização da biblioteca pygame
pygame.mixer.init() #Inicialização dos audios da biblioteca pygame
WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 900
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) #Inicial a tela
pygame.display.set_caption("GusGay") #Nome da aba

font = pygame.font.SysFont(None, 48)

#Background
image_backgroud = pygame.image.load('assets/img/fundo 1.jpg').convert()


#Passaro
PASSARO_WIDTH = 50
PASSARO_HEIGHT = 50
image_passaro1 = pygame.image.load("assets/img/passaro.png").convert_alpha()
image_passaro1 = pygame.transform.scale(image_passaro1, (PASSARO_WIDTH, PASSARO_HEIGHT)).convert_alpha()

image_passaro2 = pygame.image.load("assets/img/passaro 2.png").convert_alpha()
image_passaro2 = pygame.transform.scale(image_passaro1, (PASSARO_WIDTH, PASSARO_HEIGHT)).convert_alpha()

#Mira 
MIRA_WIDTH = 70
MIRA_HEIGHT = 70
image_mira = pygame.image.load("assets/img/mira.png").convert_alpha()
image_mira = pygame.transform.scale(image_mira, (MIRA_WIDTH, MIRA_HEIGHT)).convert_alpha()
mira_rect = image_mira.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
# Oculta o cursor do mouse
pygame.mouse.set_visible(False)


#Arma1
ARMA1_WIDTH = 400
ARMA1_HEIGHT = 400
image_arma1 = pygame.image.load('assets/img/arma1.png').convert_alpha()
image_arma1 = pygame.transform.scale(image_arma1, (ARMA1_WIDTH, ARMA1_HEIGHT))
arma1_rect = image_arma1.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 1.25))

#Arma2
ARMA2_WIDTH = 400
ARMA2_HEIGHT = 400
image_arma2 = pygame.image.load('assets/img/arma2.png').convert_alpha()
image_arma2 = pygame.transform.scale(image_arma2, (ARMA2_WIDTH, ARMA2_HEIGHT))
arma2_rect = image_arma2.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 1.25))

#Arma3
ARMA3_WIDTH = 400
ARMA3_HEIGHT = 400
image_arma3 = pygame.image.load('assets/img/arma3.png').convert_alpha()
image_arma3 = pygame.transform.scale(image_arma3, (ARMA3_WIDTH, ARMA3_HEIGHT))
arma3_rect = image_arma3.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 1.32))

#Som ambiente1
som_ambiente1 = pygame.mixer.Sound('assets/sounds/som ambiente 1.mp3')
som_ambiente1.play(-1) #Loop infinito de som ambiente

#Som ambiente2


#Som ambiente3



#Som arma1
som_arma1 = pygame.mixer.Sound('assets/sounds/tiro arma1.mp3')

#Som arma2
som_arma2 = pygame.mixer.Sound('assets/sounds/tiro arma2.mp3')

#Som arma3
som_arma3 = pygame.mixer.Sound(('assets/sounds/tiro arma3.mp3'))

#Som score
som_score = pygame.mixer.Sound('assets/sounds/score2.wav')


#Classes

#Classe que gera e atualiza os passaros
class Passaro(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img 
        self.rect = self.image.get_rect()
        self.rect.x = random.choice([0 - PASSARO_WIDTH,WINDOW_WIDTH + PASSARO_WIDTH])
        self.rect.y = random.choice([100, 180])
        if self.rect.x == (0 - PASSARO_WIDTH):
            self.speedx = random.randint(10,15)
            self.speedy = 0
        else:
            self.speedx = random.randint(10,15)
            self.speedy = 0

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.x > (WINDOW_WIDTH + PASSARO_WIDTH) or self.rect.x < (0 - PASSARO_WIDTH):
            self.rect.x = random.choice([0 - PASSARO_WIDTH, WINDOW_WIDTH + PASSARO_WIDTH])
            self.rect.y = random.choice([100, 180])
            if self.rect.x == (0 - PASSARO_WIDTH):
                self.speedx = random.randint(10, 15)
            else:
                self.speedx = random.randint(-15, -10)
                self.speedy = 0

#Grupo de passaros
all_passaros = pygame.sprite.Group()

#Criando vários passasor
for i in range(10):
    passaro = Passaro(image_passaro1)
    all_passaros.add(passaro)
        
#Limitador de FPS
clock = pygame.time.Clock()
FPS = 60

#Variaveis para serem atualizadas no Game Loop
pontos = 0

tempo_total = 30
tempo_restante = tempo_total
tempo_inicial = time.time() #Retorna o tempo atual durante o loop

pontuacao_max_1 = 2000

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
            for passaro in all_passaros:
                if passaro.rect.collidepoint(evento.pos):
                    passaro.kill()
                    pontos +=100
                    som_score.play()
    
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