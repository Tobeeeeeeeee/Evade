import pygame
import random
import sys

# Initiera pygame
pygame.init()

# Fönsterstorlek
WIDTH, HEIGHT = 400, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("evade!")

# Färger
DARK_BG = (30, 30, 30)
LIME_GREEN = (50, 205, 50)
PINK = (255, 105, 180)
BLACK = (0, 0, 0)

# Spelare
player_size = 25
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - player_size - 50
player_speed = 5
