import pygame
import random
from parametros import *

#Classe que gera e atualiza os passaros
class Passaro1(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img[0]

        self.list_img = img
        self.invertido = False

        self.rect = self.image.get_rect()
        self.rect.x = random.choice([0 - PASSARO_WIDTH,WINDOW_WIDTH + PASSARO_WIDTH])
        if self.rect.x == WINDOW_WIDTH + PASSARO_WIDTH:
            self.image = img[1]
            self.invertido = True
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
            
            if self.invertido and self.rect.x == 0 - PASSARO_WIDTH:
                self.image = self.list_img[0]
                self.invertido = False
            elif not self.invertido and self.rect.x == WINDOW_WIDTH + PASSARO_WIDTH:
                self.image = self.list_img[1]
                self.invertido = True

            self.rect.y = random.choice([100, 180])
            if self.rect.x == (0 - PASSARO_WIDTH):
                self.speedx = random.randint(10, 15)
            else:
                self.speedx = random.randint(-15, -10)
                self.speedy = 0


class Passaro2(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image_esquerda = img[1]
        self.image_direita = img[0]
        self.rect = self.image_esquerda.get_rect()

        side = random.choice(["left", "right"])  # Escolha aleatoriamente o lado de onde o pássaro aparecerá
        if side == "left":
            self.rect.x = 0 - PASSARO_WIDTH
            self.speedx = random.randint(10, 15)
            self.image = self.image_direita  # Pássaro movendo-se da esquerda para a direita
        else:
            self.rect.x = WINDOW_WIDTH + PASSARO_WIDTH
            self.speedx = random.randint(-15, -10)
            self.image = self.image_esquerda  # Pássaro movendo-se da direita para a esquerda

        self.rect.y = random.choice([100, 180])
        self.speedy = random.randint(-5, 5)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.x > (WINDOW_WIDTH + PASSARO_WIDTH) or self.rect.x < (0 - PASSARO_WIDTH):
            side = random.choice(["left", "right"])  # Escolha aleatoriamente o lado de onde o pássaro aparecerá
            if side == "left":
                self.rect.x = 0 - PASSARO_WIDTH
                self.speedx = random.randint(10, 15)
                self.image = self.image_direita  # Pássaro movendo-se da esquerda para a direita
            else:
                self.rect.x = WINDOW_WIDTH + PASSARO_WIDTH
                self.speedx = random.randint(-15, -10)
                self.image = self.image_esquerda  # Pássaro movendo-se da direita para a esquerda

            self.rect.y = random.choice([100, 180])
            self.speedy = random.randint(-5, 5)

class Passaro3(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image_esquerda = img[1]
        self.image_direita = img[0]
        self.rect = self.image_esquerda.get_rect()

        side = random.choice(["left", "right"])  # Escolha aleatoriamente o lado de onde o pássaro aparecerá
        if side == "left":
            self.rect.x = 0 - PASSARO_WIDTH
            self.speedx = random.randint(10, 15)
            self.image = self.image_direita  # Pássaro movendo-se da esquerda para a direita
        else:
            self.rect.x = WINDOW_WIDTH + PASSARO_WIDTH
            self.speedx = random.randint(-15, -10)
            self.image = self.image_esquerda  # Pássaro movendo-se da direita para a esquerda

        self.rect.y = random.choice([100, 180])
        self.speedy = random.randint(-7, 7)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.x > (WINDOW_WIDTH + PASSARO_WIDTH) or self.rect.x < (0 - PASSARO_WIDTH):
            side = random.choice(["left", "right"])  # Escolha aleatoriamente o lado de onde o pássaro aparecerá
            if side == "left":
                self.rect.x = 0 - PASSARO_WIDTH
                self.speedx = random.randint(10, 15)
                self.image = self.image_direita  # Pássaro movendo-se da esquerda para a direita
            else:
                self.rect.x = WINDOW_WIDTH + PASSARO_WIDTH
                self.speedx = random.randint(-15, -10)
                self.image = self.image_esquerda  # Pássaro movendo-se da direita para a esquerda

            self.rect.y = random.choice([100, 180])
            self.speedy = random.randint(-7, 7)


# Manga
class Manga(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()

        self.rect.x = random.choice([0 - PASSARO_WIDTH, WINDOW_WIDTH + PASSARO_WIDTH])
        if self.rect.x == WINDOW_WIDTH + PASSARO_WIDTH:
            self.speedx = random.randint(-15, -10)
        else:
            self.speedx = random.randint(10, 15)

        self.rect.y = random.choice([100, 180])
        self.speedy = random.randint(-5, 5)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.x > (WINDOW_WIDTH + PASSARO_WIDTH) or self.rect.x < (0 - PASSARO_WIDTH):
            self.rect.x = random.choice([0 - PASSARO_WIDTH, WINDOW_WIDTH + PASSARO_WIDTH])

            if self.rect.x == 0 - PASSARO_WIDTH:
                self.speedx = random.randint(10, 15)
            else:
                self.speedx = random.randint(-15, -10)

            self.rect.y = random.choice([100, 180])
            self.speedy = random.randint(-5, 5)

#Classe que gera e atualiza as explosões

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

#Classe que gera e atualiza a ponta das armas

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