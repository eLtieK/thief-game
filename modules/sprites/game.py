from config.settings import *
from config.loader import *
import pygame

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Thief')
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
    
    def stop(self):
        self.running = False

    def run(self):
        while self.running:
            # dt
            dt = self.clock.tick() / 1000

            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.stop()

            # update

            # draw
            pygame.display.update()
        
        pygame.quit()