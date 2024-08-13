import pygame
from rigidbody2d import RigidBody2D


class Character(RigidBody2D):
    def __init__(self, window, x, y, width, height, speed, jump_strength):
        super().__init__()

        self.window = window
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.jump_strength = jump_strength

    def draw(self):
        pygame.draw.rect(self.window, (255, 0, 0), (self.x, self.y, self.width, self.height))

    def move(self, keys):
        dx = 0

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            dx = 1
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            dx = -1

        self.velocity_x = self.speed * dx

        if keys[pygame.K_SPACE] and self.on_ground:
            self.velocity_y = self.jump_strength
            self.on_ground = False

        self.apply_gravity()
        self.update_position()

        if self.y >= self.window.get_height() - self.height:
            self.y = self.window.get_height() - self.height
            self.on_ground = True
            self.velocity_y = 0
