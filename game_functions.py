"""This module holds game functions in Alien Invasion."""
import sys

import pygame

from bullet import Bullet
from alien import Alien

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Respond to keypresses."""
    if event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        add_bullet(ai_settings, screen, ship, bullets)

def add_bullet(ai_settings, screen, ship, bullets):
    """Add bullet to Group of bullets if ammo limit not reached."""
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
    """Respond to keyboard and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship, aliens, bullets):
    """Draw objects and update screen."""
    screen.fill(ai_settings.bg_color)   # Draw screen.
    for bullet in bullets.sprites():    # Draw each bullet in Group
        bullet.draw_bullet()
    ship.blitme()                       # Draw ship.
    aliens.draw(screen)                 # Draw aliens.
    pygame.display.flip()           # Make most recently drawn screen visible.

def update_bullets(bullets):
    """Move bullets up screen and remove old bullets."""
    # Move bullets up screen.
    bullets.update()
    # Remove old bullets.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def create_fleet(ai_settings, screen, ship, aliens):
    """Create a fleet of aliens."""
    # Create an alien and find number of aliens in a row.
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, 
        alien.rect.height)

    # Create first row of aliens.
    for row_num in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_num)

def get_number_rows(ai_settings, ship_height, alien_height):
    """Return number of rows of aliens that fit on screen."""
    available_space_y = (
        ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def get_number_aliens_x(ai_settings, alien_width):
    """Return number of aliens that fit in a row on the screen."""
    # Space between each alien is equal to one alien width.
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Create an alien and add it to the row."""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    # Place alien in appropriate row.
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def update_aliens(aliens):
    """Update positions of all aliens."""
    aliens.update()
