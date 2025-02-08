from config.settings import *
from config.loader import *
import pygame
from modules.sprites.thief import *
from modules.sprites.audio import audio
from modules.sprites.gun import *

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Thief')
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.all_sprites = pygame.sprite.Group()
        self.thief_sprites = pygame.sprite.Group()
        self.thief_timer()
        audio.play_background_music()
        self.spawn()

    def spawn(self):
        Gun(self.all_sprites)
    
    def thief_timer(self):
        # timer
        self.thief_event = pygame.event.custom_type()
        pygame.time.set_timer(self.thief_event, 300)

    def spawn_thief(self):
        Thief((self.all_sprites, self.thief_sprites))

    def stop(self):
        self.running = False
        
    def background(self, image_path):
        image = pygame.image.load(image_path)  # Tải ảnh nền
        image = pygame.transform.scale(image, self.display_surface.get_size())  # Căn chỉnh kích thước nền
        self.display_surface.blit(image, (0, 0))  # Vẽ hình nền lên màn hình

    def kill_thief(self):
        mouse_pos = pygame.mouse.get_pos()
        for thief in self.thief_sprites:
            if thief.hitbox.collidepoint(mouse_pos):
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
                    audio.play_shoot()
                    if event.button == 1:
                        self.kill_thief()
                if event.type == self.thief_event:
                    self.spawn_thief()
            # update
            self.all_sprites.update(dt)

            # draw
            self.background(BACKGROUND_PATH)
            self.all_sprites.draw(self.display_surface)
            print(self.all_sprites)
            pygame.display.update()
        
        pygame.quit()