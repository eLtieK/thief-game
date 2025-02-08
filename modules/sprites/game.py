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
    
    # pygame mixer 
        pygame.mixer.init()  
        self.background_music = pygame.mixer.Sound(MUSIC_PATH)  
        self.background_music.set_volume(0.5)
        self.background_music.play(loops=-1, maxtime=0, fade_ms=0)
    
    def thief_timer(self):
        # timer
        self.thief_event = pygame.event.custom_type()
        pygame.time.set_timer(self.thief_event, 300)

    def spawn_thief(self):
        Thief(self.all_sprites)

    def stop(self):
        self.running = False
        
    def background(self, image_path):
        image = pygame.image.load(image_path)  # Tải ảnh nền
        image = pygame.transform.scale(image, self.display_surface.get_size())  # Căn chỉnh kích thước nền
        self.display_surface.blit(image, (0, 0))  # Vẽ hình nền lên màn hình

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
            self.background(BACKGROUND_PATH)
            self.all_sprites.draw(self.display_surface)
            print(self.all_sprites)
            pygame.display.update()
        
        pygame.quit()