import pygame


class Character:
    def __init__(self, window, x, y, width, height, speed):
        self.window = window
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed

    def draw(self):
        pygame.draw.rect(self.window, (255, 0, 0), (self.x, self.y, self.width, self.height))

    def move(self, keys):
        dx = 0
        dy = 0

        if pygame.K_w in keys or pygame.K_UP in keys:
            dy = -1
        if pygame.K_s in keys or pygame.K_DOWN in keys:
            dy = 1
        if pygame.K_d in keys or pygame.K_RIGHT in keys:
            dx = 1
        if pygame.K_a in keys or pygame.K_LEFT in keys:
            dx = -1

        self.x += self.speed * dx
        self.y += self.speed * dy
