from config import WORLD_GRAVITY


class RigidBody2D:
    def __init__(self):
        self.velocity_x = 0
        self.velocity_y = 0
        self.gravity = WORLD_GRAVITY
        self.on_ground = False
        self.x = 0
        self.y = 0

    def apply_gravity(self):
        if not self.on_ground:
            self.velocity_y += self.gravity

    def update_position(self):
        self.x += self.velocity_x
        self.y += self.velocity_y
