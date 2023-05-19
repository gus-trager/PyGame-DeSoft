import pygame
import sys
import random

#Cores
AZUL = (0, 0, 255)
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)
AMARELO = (255, 255, 0)

#Inicia Pygame e tela + nome da aba
pygame.init() #Inicialização da biblioteca pygame
WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 800
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) #Inicial a tela
pygame.display.set_caption("GusGay") #Nome da aba

font = pygame.font.SysFont(None, 48)

#Background
image_backgroud = pygame.image.load('assets/fundo.jpg').convert()


#Passaro
PASSARO_WIDTH = 50
PASSARO_HEIGHT = 50
image_passaro = pygame.image.load("assets/passaro.png").convert_alpha()
image_passaro = pygame.transform.scale(image_passaro, (PASSARO_WIDTH, PASSARO_HEIGHT)).convert_alpha()

class Passaro(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img 
        self.rect = self.image.get_rect()
        self.rect.x = random.choice([0 - PASSARO_WIDTH,WINDOW_WIDTH + PASSARO_WIDTH])
        self.rect.y = (100)
        if self.rect.x == (0 - PASSARO_WIDTH):
            self.speedx = random.randint(20,21)
            self.speedy = 0
        else:
            self.speedx = random.randint(20,21)
            self.speedy = 0

    def update(self):
        self.rect.x +=self.speedx
        self.rect.y +=self.speedy

        if self.rect.x > (WINDOW_WIDTH + PASSARO_WIDTH):
            self.rect.x = random.choice([0 - PASSARO_WIDTH,WINDOW_WIDTH + PASSARO_WIDTH])
            self.rect.y = (100)
            self.speedx = random.randint(20,21)
            self.speedy = 0


passaro1 = Passaro(image_passaro)
        

clock = pygame.time.Clock()
FPS = 30

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

    
    #Atualiza a posição dos pássaros

    window.fill((0, 0 ,0)) #Preenche a tela com a cor preta
    window.blit(image_backgroud, (0,0)) #Depois preenche com o backgroud

    window.blit(passaro1.image, (passaro1.rect))

    passaro1.update()
    pygame.display.update()

pygame.quit()