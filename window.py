import pygame
from character import Character

from config import (WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE,
                    BACKGROUND_COLOR,
                    PLAYER_DEFAULT_X, PLAYER_DEFAULT_Y,
                    PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_SPEED)


class Window:
    def __init__(self):
        self.BACKGROUND_COLOR = BACKGROUND_COLOR

        self.SCREEN_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)

        self.screen = pygame.display.set_mode(self.SCREEN_SIZE)
        pygame.display.set_caption(WINDOW_TITLE)

    def run(self):
        character = Character(self.screen, PLAYER_DEFAULT_X, PLAYER_DEFAULT_Y,
                              PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_SPEED)

        keys = []

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key not in keys:
                        keys.append(event.key)
                elif event.type == pygame.KEYUP:
                    if event.key in keys:
                        keys.remove(event.key)

            self.screen.fill(self.BACKGROUND_COLOR)

            character.move(keys)
            character.draw()

            pygame.display.flip()

        pygame.quit()
