import pygame
from mem679_snake.game import Game
from mem679_snake.config import SCREEN_WIDTH, SCREEN_HEIGHT


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Snake Game")

    game = Game(screen)
    game.run()

    pygame.quit()


if __name__ == "__main__":
    main()
