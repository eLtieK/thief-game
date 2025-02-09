from config.settings import *
from config.loader import *
import pygame
from modules.sprites.thief import *
from modules.sprites.audio import audio
from modules.sprites.gun import *
from modules.ui.ui import *

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Thief')
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

        # groups
        self.all_sprites = pygame.sprite.Group()
        self.thief_sprites = pygame.sprite.Group()

        self.thief_timer()
        audio.play_background_music()

    def spawn(self):
        self.ui = Ui(self)
        pygame.mouse.set_visible(False) 
        Gun(self.all_sprites)
        Crosshair(self.all_sprites)
    
    def thief_timer(self):
        # timer
        self.thief_event = pygame.event.custom_type()
        self.thief_time = 400
        pygame.time.set_timer(self.thief_event, self.thief_time)

    def spawn_thief(self):
        if not all(pos == 1 for pos in Thief.pos_matrix):
            Thief(self.thief_sprites)
        if len(self.thief_sprites) >= 8:
            self.ui.game_over_ui.game_over()

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
                self.ui.change_score(1)
                thief.reset_pos()
                thief.kill()

    def run(self):
        self.spawn()
        while self.running:
            # dt
            dt = self.clock.tick() / 1000

            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.ui.save_score()
                    self.stop()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        audio.play_shoot()
                        self.ui.register_click()
                        Explosion(pygame.mouse.get_pos(), self.all_sprites)
                        self.kill_thief()
                if event.type == self.thief_event:
                    self.spawn_thief()
            # update
            self.all_sprites.update(dt)

            # draw
            self.background(BACKGROUND_PATH)
            self.thief_sprites.draw(self.display_surface)
            self.ui.display_score()
            self.ui.game_over()
            self.all_sprites.draw(self.display_surface)
            pygame.display.update()
        
        self.ui.save_score()
        pygame.quit()