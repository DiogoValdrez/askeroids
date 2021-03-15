import pygame
import sys
from ship import Ship
from general_settings import General_settings
from events import Events

def run_game():
    pygame.init()
    gs = General_settings()
    ev = Events
    bg = pygame.display.set_mode((gs.bg_width, gs.bg_height))
    ship = Ship(bg)
    pygame.display.set_caption("Project A")
    while True:
        bg.fill(gs.bg_color)
        ship.blit_ship()
        ev.check_events(ship)
        #resolver bug de ter de clicar para avançar
        pygame.display.flip()

run_game()