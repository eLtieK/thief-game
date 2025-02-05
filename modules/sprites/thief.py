import pygame
import random
from config.settings import *

class Thief(pygame.sprite.Sprite):
    def __init__(self, groups, image, pos=None):
        super().__init__(groups)
        self.image = image
        if pos is None:
            pos = (random.randint(0, WINDOW_WIDTH), random.randint(0, WINDOW_HEIGHT))
        self.rect = self.image.get_frect(center = pos)
