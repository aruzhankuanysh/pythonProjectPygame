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

hero = pygame.Surface((40, 50))
hero.fill(THECOLORS['blue'])
rect = hero.get_rect()
print(rect)

screen.fill(THECOLORS['white'])
screen.blit(hero, (100, 50))
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    clock.tick(60)





