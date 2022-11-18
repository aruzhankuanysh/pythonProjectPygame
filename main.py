import pygame
import sys
from pygame.color import THECOLORS

pygame.init()

W = 1000
H = 1000
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("MyGameFox")
pygame.display.set_icon(pygame.image.load('sprites/fox/Fox1.png'))

screen.fill(THECOLORS['white'])

clock = pygame.time.Clock()

surf = pygame.Surface((200, 200))
surf.fill(THECOLORS['red'])
pygame.draw.circle(surf, THECOLORS['green'], (100, 100), 80)

surf_alpha = pygame.Surface((W, 100))
pygame.draw.rect(surf_alpha, THECOLORS['blue'], (0, 0, W, 100))
surf_alpha.set_alpha(128)

surf.blit(surf_alpha, (0, 50))
screen.blit(surf, (50, 50))

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    clock.tick(60)