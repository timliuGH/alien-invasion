"""This module holds the Ship class."""

import pygame

class Ship():
    """This is a model of a ship that fires bullets."""

    def __init__(self, screen):
        """Initialize ship and set starting location."""
        # Access game screen where ship will be drawn (via blitme function).
        self.screen = screen

        # Load ship image and get ship rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Place ship at bottom center of screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Draw ship at current location."""
        self.screen.blit(self.image, self.rect)
