"""This module holds the Bullet class."""

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """This models bullets fired from a ship."""

    def __init__(self, ai_settings, screen, ship):
        """Create a bullet object at the ship's current position."""
        # Initialize bullet from parent class.
        super().__init__()

        # Get screen on which to draw bullet.
        self.screen = screen

        # Create a bullet rect at (0, 0) initially.
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, 
            ai_settings.bullet_height)

        # Set bullet at ship's position.
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Store bullet's position as decimal value.
        self.y = float(self.rect.y)

        # Store bullet settings.
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Move bullet up the screen."""
        # Update decimal position of bullet.
        self.y -= self.speed_factor
        # Update rect value from bullet position.
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw bullet to screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
