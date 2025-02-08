import pygame
import random
from config.settings import *
from config.loader import *

class Gun(pygame.sprite.Sprite):
    def __init__(self, groups, image=None, pos=None):
        super().__init__(groups)
        if image is None:
            image = pygame.image.load(GUN_PATH).convert_alpha()
            image = pygame.transform.scale(image, (200, 200)) 

        self.image = image
        if pos is None:
            pos = pygame.mouse.get_pos()
        self.rect = self.image.get_frect(center = pos)

    def update(self, dt):
        self.rect = pygame.mouse.get_pos()

class Crosshair(pygame.sprite.Sprite):
    def __init__(self, groups, image=None, pos=None):
        super().__init__(groups)
        if image is None:
            image = pygame.image.load(CROSSHAIR_PATH).convert_alpha()
            image = pygame.transform.scale(image, (60, 60)) 

        self.image = image
        if pos is None:
            pos = pygame.mouse.get_pos()
        self.rect = self.image.get_frect(center = pos)

    def update(self, dt):
        self.rect.center = pygame.mouse.get_pos()

class Explosion(pygame.sprite.Sprite):
    def __init__(self, pos, groups, frames=None):
        super().__init__(groups)
        print(EXPLOSION_PATH)
        if frames is None:
            self.frames = [pygame.image.load(frame).convert_alpha() for frame in EXPLOSION_PATH]
        self.frames_index = 0
        self.image = self.frames[self.frames_index]
        self.rect = self.image.get_frect(center = pos)
    
    def update(self, dt):
        self.frames_index += 200 * dt
        if self.frames_index < len(self.frames):
            self.image = self.frames[int(self.frames_index)]
        else: 
            self.kill()
