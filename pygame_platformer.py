# imports
import pygame, sys
from pygame.locals import *

pygame.init()
vec = pygame.math.Vector2 # 2 for two dimensional


# colors
WHITE = (255, 255, 255)

# variables
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 450
ACC = 0.5
FRIC = -0.12
FPS = 60

CLOCK = pygame.time.Clock()


# setup display
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Platformer Game")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((128, 255, 40))
        self.rect = self.surf.get_rect(center = (10, 420))

class Platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((SCREEN_WIDTH, 20))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT -10))

PT1 = Platform()
P1 = Player()

# Loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
