import pygame
from config import config

class Tilemap():
    def __init__(self, filename ="tilemap.txt"):
        self.tilemap = self.load_tilemap(filename)

    def load_tilemap(self,filename):
        with open(filename, 'r') as file:
            return [line.strip() for line in file]

    def draw(self, screen):
    
        for y, row in enumerate(self.tilemap):
            for x, tile in enumerate(row):
                color = TILE_TYPES.get(tile, BLACK)
                pygame.draw.rect(screen, color, (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))


print("this is for testing the webhook, it will be deleted after")
    
