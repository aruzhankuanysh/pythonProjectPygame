import pygame

pygame.init()

W = 680
H = 400
sc = pygame.display.set_mode((W, H))
pygame.display.set_caption('Изображения')
pygame.display.set_icon(pygame.image.load(f'sprites/fox/Fox1.png'))

clock = pygame.time.Clock()
FPS = 60

fox_surf = pygame.image.load('sprites/fox/Fox1.png')
fox_rect = fox_surf.get_rect(center=(W // 2, H // 2))

bg_surf = pygame.image.load("C:/Users/GosUser_02/Downloads/Telegram Desktop/aaa.jpg")

sc.blit(bg_surf, (0, 0))
sc.blit(fox_surf, fox_rect)
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    clock.tick(FPS)
