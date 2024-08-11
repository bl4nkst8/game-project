import pygame


class Window:
    def __init__(self):
        self.BACKGROUND_COLOR = (234, 212, 252)

        self.SCREEN_SIZE = (300, 300)

        self.screen = pygame.display.set_mode(self.SCREEN_SIZE)
        pygame.display.set_caption("My game!")

    def run(self):
        pygame.display.flip()

        self.screen.fill(self.BACKGROUND_COLOR)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            pygame.display.flip()

        pygame.quit()
