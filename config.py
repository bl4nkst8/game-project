# Used for development
DEBUG = True

# Window constants
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Game"

BACKGROUND_COLOR = (234, 212, 252)

# Player constants
PLAYER_DEFAULT_X = 50
PLAYER_DEFAULT_Y = 50

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60

PLAYER_SPEED = 5
PLAYER_JUMP_STRENGTH = -12

# Physics constants
WORLD_GRAVITY = 0.5

# World constants
TILE_SIZE = 32
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)

TILE_TYPES = {
    '#': GRAY,   # Wall
    '.': WHITE,  # Floor
}

