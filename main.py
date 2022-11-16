import pygame
import sys
from pygame.color import THECOLORS

pygame.init()

k = 1000
m = 1000
screen = pygame.display.set_mode((k, m))
screen.fill(THECOLORS['purple'])

clock = pygame.time.Clock()
i = 0
##############################################
x = k // 2
y = m // 2
speed = 10

flLeft = flRight = flUp = flDown = False
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= speed
    elif keys[pygame.K_RIGHT]:
        x += speed
    elif keys[pygame.K_UP]:
        y -= speed
    elif keys[pygame.K_DOWN]:
        y += speed

    screen.fill(THECOLORS['purple'])
    pygame.draw.rect(screen, THECOLORS['cyan'], (x, y, 10, 20))
    pygame.display.update()
    clock.tick(60)





