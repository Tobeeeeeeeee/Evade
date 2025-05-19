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

# Hinder
obstacle_size = 40
obstacle_base_speed = 2
obstacle_multiplier = 0.05

# Lista för hinder
obstacles = []

# Spawn-timer
SPAWN_EVENT = pygame.USEREVENT + 1
spawn_interval = 300
spawn_twice_chance = 0.01
pygame.time.set_timer(SPAWN_EVENT, spawn_interval)

# Poäng
score = 0
font = pygame.font.SysFont(None, 36)

# Spelloop
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == SPAWN_EVENT:    
            # Skapa nytt hinder
            x = random.randint(0, WIDTH - obstacle_size)
            y = -obstacle_size
            obstacles.append([x, y])
            if random.random() < spawn_twice_chance:
                x = random.randint(0, WIDTH - obstacle_size)
                y = -obstacle_size
                obstacles.append([x, y])
                spawn_twice_chance -= 0.5
            
    spawn_twice_chance += 0.01
    spawn_interval = spawn_interval * obstacle_multiplier
