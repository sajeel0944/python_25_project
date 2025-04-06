import pygame
import random

pygame.font.init()

# GLOBAL VARIABLES
s_width = 800
s_height = 750
play_width = 300  # 300 // 10 = 30 width per block
play_height = 600  # 600 // 20 = 30 height per block
block_size = 30
top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height - 50

# SHAPES
S = [['.....', '.....', '..00.', '.00..', '.....'],
     ['.....', '..0..', '..00.', '...0.', '.....']]

Z = [['.....', '.....', '.00..', '..00.', '.....'],
     ['.....', '..0..', '.00..', '.0...', '.....']]

I = [['..0..', '..0..', '..0..', '..0..', '.....'],
     ['.....', '0000.', '.....', '.....', '.....']]

O = [['.....', '.....', '.00..', '.00..', '.....']]

J = [['.....', '.0...', '.000.', '.....', '.....'],
     ['.....', '..00.', '..0..', '..0..', '.....'],
     ['.....', '.....', '.000.', '...0.', '.....'],
     ['.....', '..0..', '..0..', '.00..', '.....']]

L = [['.....', '...0.', '.000.', '.....', '.....'],
     ['.....', '..0..', '..0..', '..00.', '.....'],
     ['.....', '.....', '.000.', '.0...', '.....'],
     ['.....', '.00..', '..0..', '..0..', '.....']]

T = [['.....', '..0..', '.000.', '.....', '.....'],
     ['.....', '..0..', '..00.', '..0..', '.....'],
     ['.....', '.....', '.000.', '..0..', '.....'],
     ['.....', '..0..', '.00..', '..0..', '.....']]

shapes = [S, Z, I, O, J, L, T]
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), 
                (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]

class Piece(object):
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)]
        self.rotation = 0

# Functions for the game will go here
# draw_grid, draw_window, convert_shape_format, etc.


def main():
    win = pygame.display.set_mode((s_width, s_height))
    pygame.display.set_caption('Tetris by ChatGPT')
    
    run = True
    clock = pygame.time.Clock()
    fall_time = 0

    while run:
        fall_speed = 0.27
        grid = [[(0, 0, 0) for _ in range(10)] for _ in range(20)]

        fall_time += clock.get_rawtime()
        clock.tick()

        if fall_time / 1000 >= fall_speed:
            fall_time = 0
            # Move piece down

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Drawing code here
        win.fill((0, 0, 0))
        pygame.display.update()

    pygame.quit()


main()
