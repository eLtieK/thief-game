import pygame
import random
from config.settings import *
from config.loader import *

class Thief(pygame.sprite.Sprite):
    def __init__(self, groups, image=None, pos=None):
        super().__init__(groups)
        if image is None:
            image = pygame.image.load(THIEF_PATH()).convert_alpha()
            image = pygame.transform.scale(image, (130, 130)) 

        self.image = image
        if pos is None:
            pos = Thief.random_position()
        self.rect = self.image.get_frect(center = pos)
        self.hitbox = self.rect.inflate(-50, -50)  # Thu nhỏ hitbox
   
    @staticmethod
    def random_position():
        return random.choice(THIEF_POSITION)
