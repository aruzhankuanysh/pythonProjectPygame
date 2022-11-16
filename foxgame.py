import pygame
import sys
from pygame.color import THECOLORS

pygame.init()

k = 1000
m = 1000
screen = pygame.display.set_mode((k, m))

Fox = [pygame.image.load(f"sprites/fox/Fox{i}.png") for i in range(1, 6)]
FoxRun = [pygame.image.load(f"sprites/foxrun/FoxRun{i}.png") for i in range(1, 9)]
FoxJump = [pygame.image.load(f"sprites/foxjump/FoxJump{i}.png") for i in range(1, 11)]
FoxWatch = [pygame.image.load(f"sprites/foxwatch/FoxWatch{i}.png") for i in range(1, 14)]

clock = pygame.time.Clock()
i = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        screen.fill(THECOLORS['purple'])
        keys = pygame.key.get_pressed()
        screen.blit(FoxWatch[i // 5], (100, 20))
        screen.blit(Fox[i // 12], (400, 20))
        screen.blit(FoxRun[i // 8], (100, 300))
        screen.blit(FoxJump[i // 6], (400, 300))
        i += 1
        if i == 60:
            i = 0
        pygame.display.update()
        clock.tick(60)

        ####################################################################################################
        # r = pygame.Rect(300, 100, 600, 300)
        # pygame.draw.rect(screen, (255, 0, 0), r, 0)
        # pygame.draw.line(screen, (255, 0, 0), (500, 200), (600, 300), width=50)
        #
        # pygame.draw.circle(screen, (255, 100, 200), (500, 400), 300, width=0)

        # pygame.draw.ellipse(screen, (255, 100, 200), r, width=0)

        # font = pygame.font.SysFont('couriernew', 40)
        # text = font.render(str('HELLO'), True, THECOLORS['green'])
        # screen.blit(text, (50, 50))
        ####################################################################################################
        # a = 0
        # b = 0
        # x = 70
        # z = 0
        # g = 1
        # f = k / x
        # t = m / x

        # s = pygame.Rect(a+100, b+100, x, x)
        # font = pygame.font.SysFont('couriernew', 20)

        # for j in range(1, int(t)):
        #     for i in range(int(f)):
        #         a = x * z
        #         z += 1
        #         text = font.render(str(g), True, THECOLORS['green'])
        #         screen.blit(text, (a+10, b+10))
        #         # a = x * i
        #         # i += 1
        #         g += 1
        #         s = pygame.Rect(a, b, x, x)
        #         pygame.draw.rect(screen, (255, 0, 0), s, 1)
        #     z = 0
        #     b = x * j
        #     j += 1
        ####################################################################################################
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



pygame.init()

k = 1000
m = 1000
screen = pygame.display.set_mode((k, m))
screen.fill(THECOLORS['white'])

clock = pygame.time.Clock()
i = 0
##############################################
flStarDraw = False
sp = None

pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    pressed = pygame.mouse.get_pressed()
    if pressed[0]:
        pos = pygame.mouse.get_pos()

        if sp is None:
            sp = pos

        width = pos[0] - sp[0]
        height = pos[1] - sp[1]

        screen.fill(THECOLORS['white'])
        pygame.draw.rect(screen, THECOLORS['purple'], pygame.Rect(sp[0], sp[1], width, height))
        pygame.display.update()
    else:
        sp = None

    clock.tick(60)


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





