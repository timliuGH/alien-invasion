"""This module holds the Settings class."""

class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize game settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.screen_caption = 'Alien Invasion'

        # Ship settings
        self.ship_speed_factor = 5.5

        # Bullet settings
        self.bullet_speed_factor = 7.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
