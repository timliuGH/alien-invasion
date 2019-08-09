"""This module holds the Alien class."""

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A model of a single alien in a fleet."""

    def __init__(self, ai_settings, screen):
        """Initialize the alien and set starting position."""
        # Initialize alien from parent class Sprite.
        super().__init__()

        # Access screen on which to draw alien.
        self.screen = screen

        # Access game settings.
        self.ai_settings = ai_settings

        # Load alien image.
        self.image = pygame.image.load('images/alien.bmp')

        # Get alien's rect.
        self.rect = self.image.get_rect()

        # Start alien at top left of screen with buffer equal to alien size.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store alien's exact horizontal position in decimal.
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw alien at current location."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Move alien."""
        self.x += (self.ai_settings.alien_speed_factor * 
                        self.ai_settings.alien_direction) 
        self.rect.x = self.x

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
