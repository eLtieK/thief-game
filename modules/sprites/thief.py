import pygame

class Thief(pygame.sprite.Sprite):
    def __init__(self, groups, pos, image):
        super().__init__(groups)
        self.image = image
        self.rect = self.image.get_frect(center = pos)
