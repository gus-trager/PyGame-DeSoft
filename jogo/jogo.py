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



#Background tele inicial
image_tela_inicio = pygame.image.load('assets/img/fundo_inicio.jpg').convert()

#Background lvl1
image_backgroud = pygame.image.load('assets/img/fundo 1.jpg').convert()

#Sapiro
SAPIRO_WIDTH = 170
SAPIRO_HEIGHT = 170
image_sapiro = pygame.image.load('assets/img/sapiro.jpg')
image_sapiro = pygame.transform.scale(image_sapiro, (SAPIRO_WIDTH, SAPIRO_HEIGHT)).convert()

#Zorzi
ZORZI_WIDHT = 170
ZORZI_HEIGHT = 170
image_zorzi = pygame.image.load('assets/img/zorzi.jpg')
image_zorzi = pygame.transform.scale(image_zorzi,(ZORZI_WIDHT, ZORZI_HEIGHT)).convert()

#Gus
GUS_WIDHT = 170
GUS_HEIGHT = 170
image_gus = pygame.image.load('assets/img/gus.jpg')
image_gus = pygame.transform.scale(image_gus,(GUS_WIDHT, GUS_HEIGHT)).convert()

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

#Titulo do jogo
fonte_titulo = 'assets/img/fonte titulo1.ttf'

#Instrucoes do jogo
fonte_instrucoes = 'assets/img/fonte instrucoes.TTF'

########################################################################## Funções ##############################################################################################

#Função da tela de inicio
def tela_inicio():
    tela_inicio = True

    window.fill(PRETO)
    window.blit(image_tela_inicio, (0,0))

    fonte_tt = pygame.font.Font(fonte_titulo, 80)
    texto_titulo = fonte_tt.render("Carecas-Strike", True, VERMELHO)
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

########################################################################### Classes ############################################################################################################

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


class Explosao(pygame.sprite.Sprite):
    def __init__(self, centro, assets):
        pygame.sprite.Sprite.__init__(self)

        #Animação da explosão
        self.explosion_anim = assets['explosion_anim']
        
        self.frame = 0
        self.image = self.explosion_anim[self.frame] #Primeira imagem, ja que o frame está em 0 (lembrar de atulizar-lo no update)
        self.rect = self.image.get_rect()
        self.rect.center = centro #Centro da imagem

        self.ultimo_update = pygame.time.get_ticks()

        self.max_ticks = 50

    def update(self):
        atual = pygame.time.get_ticks()

        passado = atual - self.ultimo_update

        if passado > self.max_ticks:
            self.ultimo_update = atual
            self.frame +=1

            if self.frame == len(self.explosion_anim):
                self.kill()
            else:
                centro = self.rect.center
                self.image = self.explosion_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = centro

class Ponta_arma(pygame.sprite.Sprite):
    def __init__(self,posicao, assets):
        pygame.sprite.Sprite.__init__(self)

        self.ponta_arma = assets['ponta_arma']

        self.frame = 0
        self.image = self.ponta_arma[self.frame] #Primeira imagem, ja que o frame está em 0 (lembrar de atulizar-lo no update)
        self.rect = self.image.get_rect(center=posicao)
          

        self.ultimo_update = pygame.time.get_ticks()

        self.max_ticks = 50

    def update(self):
        atual = pygame.time.get_ticks()

        passado = atual - self.ultimo_update

        if passado > self.max_ticks:
            self.ultimo_update = atual
            self.frame +=1

        if self.frame == len(self.ponta_arma):
            self.kill()
        else:
            centro = self.rect.center
            self.image = self.ponta_arma[self.frame]
            self.rect = self.image.get_rect()
            self.rect.center = centro
        
###################################################################################################################################################################################################
        
#Grupo de passaros
all_passaros = pygame.sprite.Group()

#Criando vários passasor
for i in range(10):
    passaro = Passaro(image_passaro1)
    all_passaros.add(passaro)
        
#Limitador de FPS
clock = pygame.time.Clock()
FPS = 60


#Valores de tamanho
ponta_arma_x = 690
ponta_arma_y = 600

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