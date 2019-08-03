import sys

import pygame

from settings import Settings
from ship import Ship

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
        # Listen for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Draw screen.
        screen.fill(ai_settings.bg_color)

        # Draw ship.
        ship.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()

run_game()
