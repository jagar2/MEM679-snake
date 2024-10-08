import pygame
from config import BLOCK_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT, GREEN


class Snake:


    """
    A class to represent the Snake in the game.

    Attributes:
        body (list of tuple): The coordinates of the snake's body segments.
        direction (str): The current direction of the snake's movement.
        new_block (bool): Flag to indicate if a new block should be added to the snake's body.

    Methods:
        __init__():
            Initializes the snake with a default body and direction.
        get_head_position():
            Returns the position of the snake's head.
        get_head_rect():
            Returns the rectangle representing the snake's head.
        change_direction(new_direction):
            Changes the direction of the snake's movement.
        move():
            Moves the snake in the current direction.
        grow():
            Sets the flag to add a new block to the snake's body.
        check_collision_with_self():
            Checks if the snake has collided with itself.
        check_collision_with_walls():
            Checks if the snake has collided with the walls.
        draw(screen):
            Draws the snake on the given screen.
    """
    def __init__(self):
        """
        Initializes the Snake object with a default body and direction.

        Attributes:
            body (list of tuple): A list of coordinates representing the snake's body segments.
            direction (str): The current direction of the snake's movement.
            new_block (bool): A flag indicating whether a new block should be added to the snake's body.
        """
        self.body = [(100, 50), (80, 50), (60, 50)]
        self.direction = "RIGHT"
        self.new_block = False

    def get_head_position(self):
        return self.body[0]

    def get_head_rect(self):
        x, y = self.get_head_position()
        return pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)

    def change_direction(self, new_direction):
        opposite_directions = {
            "UP": "DOWN",
            "DOWN": "UP",
            "LEFT": "RIGHT",
            "RIGHT": "LEFT",
        }
        if new_direction != opposite_directions.get(self.direction):
            self.direction = new_direction

    def move(self):
        x, y = self.get_head_position()

        if self.direction == "UP":
            y -= BLOCK_SIZE
        elif self.direction == "DOWN":
            y += BLOCK_SIZE
        elif self.direction == "LEFT":
            x -= BLOCK_SIZE
        elif self.direction == "RIGHT":
            x += BLOCK_SIZE

        new_head = (x, y)
        self.body.insert(0, new_head)

        if not self.new_block:
            self.body.pop()
        else:
            self.new_block = False

    def grow(self):
        self.new_block = True

    def check_collision_with_self(self):
        return self.get_head_position() in self.body[1:]

    def check_collision_with_walls(self):
        x, y = self.get_head_position()
        return x < 0 or x >= SCREEN_WIDTH or y < 0 or y >= SCREEN_HEIGHT

    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(
                screen,
                GREEN,
                pygame.Rect(segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE),
            )
