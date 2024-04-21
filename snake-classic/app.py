import pygame

from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from game_state import GameState

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()


def main():
    game_state = GameState(screen, clock)

    while True:
        game_state.update()


if __name__ == "__main__":
    main()
