import pygame
from config.loader import *
from modules.sprites.game import *
from modules.sprites.thief import *
from config.settings import *
from modules.sprites.audio import audio

class Intro(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.running = True
        self.display_surface = self.game.display_surface
        self.clock = self.game.clock
        self.play_image = pygame.image.load(INTRO_PATHS["begin_image"]).convert_alpha() 
        self.play_image_red = pygame.image.load(INTRO_PATHS["begin_image_red"]).convert_alpha()
        self.play_image = pygame.transform.scale(self.play_image, (WINDOW_WIDTH, WINDOW_HEIGHT))  
        self.play_image_red = pygame.transform.scale(self.play_image_red, (WINDOW_WIDTH, WINDOW_HEIGHT))  
        self.button_rect = pygame.Rect(285, 650, 150, 50)  
        self.is_button_pressed = False
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self)

    def draw(self):
        if self.is_button_pressed:
            self.display_surface.blit(self.play_image_red, (0, 0))
        else:
            self.display_surface.blit(self.play_image, (0, 0))

        pygame.display.update()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.game.stop()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.button_rect.collidepoint(event.pos): 
                    self.is_button_pressed = True 
                    audio.play_click()

            if event.type == pygame.MOUSEBUTTONUP:
                if self.is_button_pressed: 
                    self.is_button_pressed = False
                    self.transition_to_game()

    def transition_to_game(self):
        self.running = False
        self.game.run()

    def run(self):
        while self.running:
            self.clock.tick(60) 
            self.draw()
            self.check_events()
            
            
