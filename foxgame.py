import pygame
import sys
from pygame.color import THECOLORS

pygame.init()

k = 1000
m = 1000
screen = pygame.display.set_mode((k, m))

Fox = [pygame.image.load(f"C:/Users/GosUser_02/pythonProjectPygame/sprites/fox/Fox{i}.png") for i in range(1, 6)]
FoxWatch = [pygame.image.load(f"C:/Users/GosUser_02/pythonProjectPygame/sprites/foxwatch/FoxWatch{i}.png") for i in range(1, 14)]
FoxRun = [pygame.image.load(f"C:/Users/GosUser_02/pythonProjectPygame/sprites/foxrun/FoxRun{i}.png") for i in range(1, 9)]
FoxJump = [pygame.image.load(f"C:/Users/GosUser_02/pythonProjectPygame/sprites/foxjump/FoxJump{i}.png") for i in range(1, 11)]

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