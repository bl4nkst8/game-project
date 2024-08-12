import pygame

x = 50
y = 50
width = 40
height = 60
vel = 5


class Character:
    def __init__(self):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel
    
    def run(self):

        running = True
        while running:
            pygame.time.delay(100)

            pygame.draw.rect(self, (255, 0, 0), (x, y, width, height))
            pygame.display.update()