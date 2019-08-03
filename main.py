import sys

import pygame

def run_game():
    # Initialize pygame
    pygame.init()

    # Create screen object.
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption('Alien Invasion')

    # Start main event loop.
    while True:
        # Listen for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Make the most recently drawn screen visible.
        pygame.display.flip()

run_game()
