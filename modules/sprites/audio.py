from config.loader import *
from config.settings import *
import pygame

class Audio:
    def __init__(self):
        pygame.mixer.init()  
        self.background_music = pygame.mixer.Sound(MUSIC_PATH)  
        self.click = pygame.mixer.Sound(CLICK_PATH)  
        self.shoot = pygame.mixer.Sound(SHOOT_PATH)  
        self.setup()

    def setup(self):
        self.background_music.set_volume(0.5)
        self.shoot.set_volume(0.5)

    def play_background_music(self):
        self.background_music.play(loops=-1, maxtime=0, fade_ms=0)

    def play_click(self):
        self.click.play()

    def play_shoot(self):
        self.shoot.play()

audio = Audio()