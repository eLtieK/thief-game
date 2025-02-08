import pygame
from config.settings import *
from config.loader import *
import os

class Ui:
    def __init__(self, display_surface):
        self.display_surface = display_surface
        self.best_score = self.load_score()
        self.score = 0
        self.font = pygame.font.Font(None, 36)

    def draw_text_with_outline(self, text, position, text_color, outline_color):
        outline_surface = self.font.render(text, True, outline_color)
        text_surface = self.font.render(text, True, text_color)

        x, y = position
        for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2)]:
            self.display_surface.blit(outline_surface, (x + dx, y + dy))  # Vẽ viền

        self.display_surface.blit(text_surface, position)  # Vẽ chữ chính

    def display_score(self):
        self.draw_text_with_outline(f"Score: {self.score}", (10, 10), (230, 230, 230), (0, 0, 0))
        self.draw_text_with_outline(f"Best Score: {self.best_score}", (10, 40), (230, 230, 230), (0, 0, 0))

    def change_score(self, score):
        self.score += score
        if self.best_score <= self.score:
            self.best_score = self.score
    
    def save_score(self):
        with open(SCORE_PATH, "w") as file:
            file.write(str(self.best_score))

    def load_score(self):
        if os.path.exists(SCORE_PATH):
            with open(SCORE_PATH, "r") as file:
                content = file.read().strip()
                if content.isdigit():  
                    return int(content)
        return 0  