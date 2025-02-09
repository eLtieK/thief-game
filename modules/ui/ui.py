import pygame
from config.settings import *
from config.loader import *
from modules.sprites.thief import *
import os

class Ui:
    score = 0
    total_clicks = 0

    def __init__(self, game):
        self.best_score = self.load_score()
        self.display_surface = game.display_surface
        self.font = pygame.font.Font(None, 36)
        self.game_over_ui = GameOver(game)

    def draw_text_with_outline(self, text, position, text_color, outline_color):
        outline_surface = self.font.render(text, True, outline_color)
        text_surface = self.font.render(text, True, text_color)

        x, y = position
        for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2)]:
            self.display_surface.blit(outline_surface, (x + dx, y + dy))  # Vẽ viền

        self.display_surface.blit(text_surface, position)  # Vẽ chữ chính

    def display_score(self):
        self.draw_text_with_outline(f"Score: {Ui.score}", (10, 10), (230, 230, 230), (0, 0, 0))
        self.draw_text_with_outline(f"Best Score: {self.best_score}", (10, 40), (230, 230, 230), (0, 0, 0))
        # Tính Accuracy
        accuracy = (Ui.score / Ui.total_clicks * 100) if Ui.total_clicks > 0 else 0
        self.draw_text_with_outline(f"Accuracy: {accuracy:.2f}%", (10, 70), (255, 215, 0), (0, 0, 0))

    def change_score(self, score):
        if not self.game_over_ui.is_game_over:
            Ui.score += score
            if self.best_score <= Ui.score:
                self.best_score = Ui.score
    
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
    
    def game_over(self):
        self.game_over_ui.draw()

    def register_click(self):
        if not self.game_over_ui.is_game_over:
            Ui.total_clicks += 1
    
class GameOver():
    def __init__(self, game):
        self.game = game
        self.is_game_over = False
        self.display_surface = game.display_surface
        self.font = pygame.font.Font(None, 50)
        self.big_font = pygame.font.Font(None, 100)

    # Hàm thoát game
    def quit_game(self):
        self.game.running = False

    # Hàm chơi lại (có thể đặt lại biến và restart game)
    def restart_game(self):
        self.game.thief_sprites.empty()
        Thief.reset_matrix()
        Ui.score = 0
        Ui.total_clicks = 0
        self.is_game_over = False # Gọi lại game chính

    def draw_text_with_outline(self, text, position, text_color, outline_color):
        outline_surface = self.big_font.render(text, True, outline_color)
        text_surface = self.big_font.render(text, True, text_color)

        text_rect = text_surface.get_rect(center=position) 

        for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2)]:
            self.display_surface.blit(outline_surface, (text_rect.x + dx, text_rect.y + dy))  # Vẽ viền

        self.display_surface.blit(text_surface, text_rect)  # Vẽ chữ chính

    def draw_button(self, text, x, y, w, h, color, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        pygame.draw.rect(self.display_surface, color, (x, y, w, h))
        
        text_surface = self.font.render(text, True, (255,255,255))
        text_rect = text_surface.get_rect(center=(x + w//2, y + h//2))
        self.display_surface.blit(text_surface, text_rect)

        # Kiểm tra nếu click vào nút
        if x < mouse[0] < x + w and y < mouse[1] < y + h:
            if click[0] == 1 and action:
                action()

    def game_over(self):
        self.is_game_over = True

    def game_over_screen(self):
        # Hiển thị chữ "Game Over"
        self.draw_text_with_outline("Game Over",  (WINDOW_WIDTH/2, 200), (200, 0, 0), (0, 0, 0))

        # Vẽ nút
        self.draw_button("Play Again", WINDOW_WIDTH/2 - 100, 350, 200, 50, (0,200,0), self.restart_game)
        self.draw_button("Quit", WINDOW_WIDTH/2 - 100, 450, 200, 50, (200,0,0), self.quit_game)
    
    def draw(self):
        if self.is_game_over:
            self.game_over_screen()