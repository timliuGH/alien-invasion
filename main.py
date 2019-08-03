import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # Initialize pygame.
    pygame.init()

    # Get game settings.
    ai_settings = Settings()

    # Set up screen object.
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption(ai_settings.screen_caption)

    # Make a ship.
    ship = Ship(screen)

    # Start main event loop.
    while True:
        gf.check_events()                   
        gf.update_screen(ai_settings, screen, ship)

run_game()
