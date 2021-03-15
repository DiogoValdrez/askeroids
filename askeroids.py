import pygame
import sys

pygame.init()
scr = pygame.display.set_mode([1200,800])
scr_rect = scr.get_rect()
pygame.display.set_caption("Asteroids")
clock =  pygame.time.Clock()
font = pygame.font.SysFont("bahnschrift",25)

#scr_useful = (scr_rect.centerx, scr_rect.centery)


image = pygame.image.load('images/ship.bmp')
image = pygame.transform.scale(image, (60, 48))
rect = image.get_rect()
rect.center = scr_rect.center

#arranajr rotação


def run_game():
    game_on = True
    prov_image = image
    rotation = 0
    while game_on:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #game_on = False
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
                if event.key == pygame.K_RIGHT:
                    prov_image = pygame.transform.rotozoom(image, rotation-10, 1)
                    rotation -= 10
                    #a imagem tá a ficar desfocada e a rodar para baixo

        scr.fill((0,0,0))
        scr.blit(prov_image, rect.center)
        pygame.display.update()
        clock.tick(50)

                    

run_game()