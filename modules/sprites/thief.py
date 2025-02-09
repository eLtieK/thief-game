import pygame
import random
from config.settings import *
from config.loader import *

class Thief(pygame.sprite.Sprite):
    pos_matrix = [
        0, 0, 0, 0,
        0, 0, 0, 0,
        0, 0, 0, 0,
        0, 0, 0, 0
    ]

    def __init__(self, groups, image=None, pos=None):
        super().__init__(groups)
        if image is None:
            image = pygame.image.load(THIEF_PATH()).convert_alpha()
            image = pygame.transform.scale(image, (130, 130)) 

        self.image = image
        if pos is None:
            index, pos = Thief.random_position()
        self.index = index
        self.rect = self.image.get_frect(center = pos)
        self.hitbox = self.rect.inflate(-50, -50)  # Thu nhỏ hitbox
   
    @staticmethod
    def random_position():
        index = random.randint(0, len(THIEF_POSITION) - 1)
        while Thief.pos_matrix[index] == 1:
            index = index = random.randint(0, len(THIEF_POSITION) - 1)

        value = THIEF_POSITION[index]
        Thief.pos_matrix[index] = 1
        return index, value
    
    @staticmethod
    def reset_matrix():
        Thief.pos_matrix = [0 for i in range(16)]

    def reset_pos(self):
        Thief.pos_matrix[self.index] = 0
