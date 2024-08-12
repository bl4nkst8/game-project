import pygame

x = 50
y = 50
width = 40
height = 60
vel = 5


class Character:
    def __init__(self, window):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel
        self.window = window
    
    def run(self):

        running = True
        while running:
            pygame.time.delay(100)

            pygame.draw.rect(self.window, (255, 0, 0), (x, y, width, height))
            pygame.display.update()