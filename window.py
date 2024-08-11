import pygame

class Window:
  def __init__(self):
    BACKGROUND_COLOR = (234, 212, 252)
    SCREEN_SIZE = (300, 300)
  
    self.screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("My game!")

  def run():
    pygame.display.flip()
    
    running = True
    while running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
      
      pygame.display.flip()
    
    pygame.exit()