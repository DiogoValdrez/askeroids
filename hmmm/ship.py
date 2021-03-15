import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self, bg):
        super().__init__()

        self.bg = bg
        self.bg_rect = bg.get_rect()

        self.image = pygame.image.load('images/ship.bmp')
        self.image = pygame.transform.scale(self.image, (60, 48))
        self.image = pygame.transform.rotate(self.image, 20)# isto apenas roda a imagem, teho de rodar o retangulo, arranjar resposta
        self.rect = self.image.get_rect()

        self.rect.centerx = self.bg_rect.centerx
        self.rect.centery = self.bg_rect.centery
        
        self.error = 0
        self.ship_position()

    def blit_ship(self):
        self.bg.blit(self.image, self.rect)

    def ship_position(self):
        if (self.rect.midtop[0] - self.rect.center[0]) != 0:
            self.error = 0
            self.diag = (self.rect.midtop[1] - self.rect.center[1])/(self.rect.midtop[0] - self.rect.center[0])
            self.b = self.rect.centery - (self.diag * self.rect.centerx)
        else:
            self.error = 1  
        

    def advance(self):
        if self.error == 0:
            self.rect.centerx = self.rect.centerx + 1# tem que se trocar o 1, pq V0 é relativo à velocidade inicial x
            self.rect.centery = self.diag * self.rect.centerx + self.b
        else:
            self.rect.centerx = self.rect.centerx
            self.rect.centery = self.rect.centery - 1