import pygame
from snake import Snake
from food import Food
from config import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK, FPS

class Game:
    """
    A class to represent the Snake game.
    Attributes
    ----------
    screen : pygame.Surface
        The surface on which the game is drawn.
    clock : pygame.time.Clock
        The clock object to control the game's frame rate.
    snake : Snake
        The snake object representing the player.
    food : Food
        The food object that the snake eats.
    score : int
        The player's score.
    running : bool
        A flag to indicate if the game is running.
    Methods
    -------
    handle_events():
        Handles user input events such as key presses and window close events.
    update():
        Updates the game state, including moving the snake, checking for collisions, and handling food consumption.
    draw():
        Draws the game elements (snake, food) on the screen.
    run():
        The main game loop that runs the game, handling events, updating the game state, and drawing the screen.
    """

    def __init__(self, screen):
        """
        Initializes the game with the given screen.

        Args:
            screen (pygame.Surface): The surface on which the game will be drawn.

        Attributes:
            screen (pygame.Surface): The surface on which the game is drawn.
            clock (pygame.time.Clock): The clock object to manage the game's frame rate.
            snake (Snake): The snake object representing the player.
            food (Food): The food object that the snake will eat.
            score (int): The current score of the game.
            running (bool): A flag indicating whether the game is running.
        """
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.snake = Snake()
        self.food = Food()
        self.score = 0
        self.running = True

    def handle_events(self):
        """
        Handles the events captured by Pygame.

        This method processes events from the Pygame event queue. It handles
        the following events:
        - QUIT: Sets the running flag to False to exit the game loop.
        - KEYDOWN: Changes the direction of the snake based on the arrow key pressed.

        The direction changes are as follows:
        - UP arrow key: Changes the snake's direction to "UP".
        - DOWN arrow key: Changes the snake's direction to "DOWN".
        - LEFT arrow key: Changes the snake's direction to "LEFT".
        - RIGHT arrow key: Changes the snake's direction to "RIGHT".
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.change_direction("UP")
                elif event.key == pygame.K_DOWN:
                    self.snake.change_direction("DOWN")
                elif event.key == pygame.K_LEFT:
                    self.snake.change_direction("LEFT")
                elif event.key == pygame.K_RIGHT:
                    self.snake.change_direction("RIGHT")

    def update(self):
        """
        Update the game state by moving the snake, checking for collisions, and handling food consumption.
        This method performs the following actions:
        1. Moves the snake.
        2. Checks for collisions with walls or itself. If a collision is detected, the game stops running.
        3. Checks if the snake's head collides with the food. If a collision is detected, the snake grows, the score is incremented, and the food is respawned.
        """
        self.snake.move()
        
        # Check for wall collisions
        if self.snake.check_collision_with_walls() or self.snake.check_collision_with_self():
            self.running = False
        
        # Check if snake's head collides with food
        if self.snake.get_head_position() == self.food.position:
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
