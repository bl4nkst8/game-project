import pygame


class Character:
    def __init__(self, window, x, y, width, height, velocity):
        self.window = window
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = velocity

    def draw(self):
        pygame.draw.rect(self.window, (255, 0, 0), (self.x, self.y, self.width, self.height))
        pygame.display.update()

    def movement(self, dx, dy):
        self.x += self.vel * dx
        self.y += self.vel * dy
  


