import pygame
from character import Character
from tilemap import Tilemap

from config import (WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE,
                    BACKGROUND_COLOR,
                    PLAYER_DEFAULT_X, PLAYER_DEFAULT_Y,
                    PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_SPEED, PLAYER_JUMP_STRENGTH,
                    DEBUG)


class Window:
    def __init__(self):
        self.BACKGROUND_COLOR = BACKGROUND_COLOR

        self.SCREEN_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)

        self.screen = pygame.display.set_mode(self.SCREEN_SIZE)
        pygame.display.set_caption(WINDOW_TITLE)

    def run(self):
        character = Character(self.screen, PLAYER_DEFAULT_X, PLAYER_DEFAULT_Y,
                              PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_SPEED, PLAYER_JUMP_STRENGTH)

        clock = pygame.time.Clock()
        last_fps_count = 0

        running = True
        while running:
            if DEBUG and int(clock.get_fps()) != last_fps_count:
                last_fps_count = int(clock.get_fps())
                pygame.display.set_caption(f'{WINDOW_TITLE} - {last_fps_count}FPS')

            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill(self.BACKGROUND_COLOR)

            character.move(keys)
            character.draw()

            pygame.display.flip()
            clock.tick(60)

        pygame.quit()
