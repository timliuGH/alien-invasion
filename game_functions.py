"""This module holds game functions in Alien Invasion."""
import sys

import pygame

def check_events():
    """Respond to keyboard and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings, screen, ship):
    screen.fill(ai_settings.bg_color)   # Draw screen.
    ship.blitme()                       # Draw ship.
    pygame.display.flip()           # Make most recently drawn screen visible.
