import pygame


class EventListener:
    def __init__(self):
        self.keys = []

    def cycle(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key not in self.keys:
                    self.keys.append(event.key)
            elif event.type == pygame.KEYUP:
                if event.key in self.keys:
                    self.keys.remove(event.key)

    def player_movement_event(self):
        movement_delta = [0, 0]
        if pygame.K_w or pygame.K_DOWN in self.keys:
            movement_delta[0] = 1
        if pygame.K_s or pygame.K_UP in self.keys:
            movement_delta[0] = -1
        if pygame.K_d or pygame.K_RIGHT in self.keys:
            movement_delta[1] = 1
        if pygame.K_a or pygame.K_LEFT in self.keys:
            movement_delta[1] = -1

        return movement_delta
