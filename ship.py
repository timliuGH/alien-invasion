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

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Move ship based on movement flag."""
        # Use if instead of elif for better transition between left/right
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1

    def blitme(self):
        """Draw ship at current location."""
        self.screen.blit(self.image, self.rect)
