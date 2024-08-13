import pygame
from eventlistener import EventListener
from character import Character


class Window:
    def __init__(self):
        self.BACKGROUND_COLOR = (234, 212, 252)

        self.SCREEN_SIZE = (300, 300)

        self.screen = pygame.display.set_mode(self.SCREEN_SIZE)
        pygame.display.set_caption("My game!")

    def run(self):
        event_listener = EventListener()
        character = Character(self.screen, 50, 50, 40, 60, 5)
        pygame.display.flip()

        self.screen.fill(self.BACKGROUND_COLOR)

        running = True
        while running:
            event_listener.cycle()

            character.draw()

            pygame.display.flip()

        pygame.quit()
