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
        gf.check_events()                   # Listen for events.
        screen.fill(ai_settings.bg_color)   # Draw screen.
        ship.blitme()                       # Draw ship.

        pygame.display.flip()   # Make the most recently drawn screen visible.

run_game()
