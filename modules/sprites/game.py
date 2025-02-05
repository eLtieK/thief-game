from config.settings import *
from config.loader import *
import pygame
from modules.sprites.thief import *

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Thief')
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.all_sprites = pygame.sprite.Group()
        self.thief_timer()
    
    def thief_timer(self):
        # timer
        self.thief_event = pygame.event.custom_type()
        pygame.time.set_timer(self.thief_event, 300)

    def spawn_thief(self):
        thief_image = pygame.Surface((50,50))
        thief_image.fill((255,0,0))
        Thief(self.all_sprites, thief_image)

    def stop(self):
        self.running = False
        
    def background(self):
        self.display_surface.fill((255,255,255))

    def kill_thief(self):
        mouse_pos = pygame.mouse.get_pos()
        for thief in self.all_sprites:
            print(thief.rect.center)
            if thief.rect.collidepoint(mouse_pos):
                thief.kill()

    def run(self):
        while self.running:
            # dt
            dt = self.clock.tick() / 1000

            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.stop()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.kill_thief()
                if event.type == self.thief_event:
                    self.spawn_thief()
            # update

            # draw
            self.background()
            self.all_sprites.draw(self.display_surface)
            print(self.all_sprites)
            pygame.display.update()
        
        pygame.quit()