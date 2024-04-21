import pygame
import sys

from constants import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK, RED
from snake import Snake
from food import Food


class GameState:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.reset()

    def reset(self):
        self.snake = Snake()
        self.food = Food()
        self.score = 0
        self.game_over = False

    def update(self):
        self.screen.fill(BLACK)

        if self.game_over:
            self.show_game_over_screen()
        else:
            self.snake.handle_keys()
            if self.snake.move():
                self.game_over = True
            if self.snake.get_head_position() == self.food.position:
                self.snake.length += 1
                self.score += 1
                self.food.randomize_position()

            self.snake.draw(self.screen)
            self.food.draw(self.screen)
            text = pygame.font.SysFont('arial', 36).render(f'Score: {self.score}', True, WHITE)
            self.screen.blit(text, (5, 5))

        pygame.display.update()
        self.clock.tick(10)

    def show_game_over_screen(self):
        font = pygame.font.SysFont('arial', 72)
        game_over_text = font.render("Game Over", True, RED)
        try_again_text = pygame.font.SysFont('arial', 36).render("Try Again", True, WHITE)

        game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3))
        try_again_rect = try_again_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))

        self.screen.blit(game_over_text, game_over_rect)
        self.screen.blit(try_again_text, try_again_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if try_again_rect.collidepoint(event.pos):
                    self.reset()
