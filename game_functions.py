"""This module holds game functions in Alien Invasion."""
import sys

import pygame

from bullet import Bullet

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

def update_screen(ai_settings, screen, ship, bullets):
    """Draw objects and update screen."""
    screen.fill(ai_settings.bg_color)   # Draw screen.
    for bullet in bullets.sprites():    # Draw each bullet in Group
        bullet.draw_bullet()
    ship.blitme()                       # Draw ship.
    pygame.display.flip()           # Make most recently drawn screen visible.

def update_bullets(bullets):
    """Move bullets up screen and remove old bullets."""
    # Move bullets up screen.
    bullets.update()
    # Remove old bullets.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
