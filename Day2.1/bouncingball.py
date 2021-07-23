import pygame, sys
from pygame.locals import *

pygame.init()

RESOLUTION = (800,600)
DISPLAYSURF = pygame.display.set_mode(RESOLUTION)
BLUE  = (  0,   0, 255)
BLACK = (  0,   0,   0)
y = 300
direction = 1

 #(surface, color, center, radius, thickness)

while True:
    DISPLAYSURF.fill(BLACK)
    pygame.draw.circle(DISPLAYSURF, BLUE, (400, y), 100, 0)
    pygame.display.update()
    if y == 600:
        direction = -1
    elif y == 0:
        direction = 1
    y = y + direction

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()