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
