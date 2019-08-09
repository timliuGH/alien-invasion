import pygame
from pygame.sprite import Group

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
    ship = Ship(ai_settings, screen)

    # Make a Group (from pygame.sprite) of bullets.
    bullets = Group()

    # Make a Group of aliens.
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Start main event loop.
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
        # Check aliens after bullets to see if bullets hit aliens.
        gf.update_aliens(ai_settings, aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()
