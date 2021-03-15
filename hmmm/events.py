import pygame
import sys
from ship import Ship

class Events():
    def __init__(ship):
        ship = Ship()
    def check_events(ship):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()
                    if event.key == pygame.K_UP:
                        ship.advance()

