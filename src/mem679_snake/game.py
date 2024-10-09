import pygame
from mem679_snake.snake import Snake
from mem679_snake.food import Food
from mem679_snake.config import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK, FPS


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.snake = Snake()
        self.food = Food()
        self.score = 0
        self.running = True

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_UP, pygame.K_w):
                    self.snake.change_direction("UP")
                elif event.key in (pygame.K_DOWN, pygame.K_s):
                    self.snake.change_direction("DOWN")
                elif event.key in (pygame.K_LEFT, pygame.K_a):
                    self.snake.change_direction("LEFT")
                elif event.key in (pygame.K_RIGHT, pygame.K_d):
                    self.snake.change_direction("RIGHT")

    def update(self):
        self.snake.move()

        if (
            self.snake.check_collision_with_walls()
            or self.snake.check_collision_with_self()
        ):
            self.running = False

        if self.snake.get_head_rect().colliderect(self.food.get_rect()):
            self.snake.grow()
            self.score += 1
            self.food.respawn()

    def draw(self):
        self.screen.fill(BLACK)
        self.snake.draw(self.screen)
        self.food.draw(self.screen)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
