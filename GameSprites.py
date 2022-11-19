import pygame
from ball import Ball
from random import randint

pygame.init()
pygame.time.set_timer(pygame.USEREVENT, 1000)

pygame.mixer.music.load('sounds/fonmusic.mp3')
pygame.mixer.music.play(-1)
black = (0, 0, 0)
W, H = 1000, 570

sc = pygame.display.set_mode((W, H)) #создаем окно для отображения игры

clock = pygame.time.Clock() #для обновления окна
FPS = 60

score = pygame.image.load('sprites/balls/score_bg.png').convert_alpha()
f = pygame.font.SysFont('arial', 30)

bg = pygame.image.load('sprites/balls/bg.jpg') #загружаем фон

telega = pygame.image.load('sprites/balls/korzina.png').convert_alpha()
t_rect = telega.get_rect(centerx=W//2, bottom=H-5)

# balls_images = ['ball1.png', 'ball2.png', 'ball3.png']
balls_data = ({'path': 'ball1.png', 'score': 100},
              {'path': 'ball2.png', 'score': 150},
              {'path': 'ball3.png', 'score': 200})
balls_surf = [pygame.image.load('sprites/balls/'+data['path']).convert_alpha() for data in balls_data]

def createBall(group):
    indx = randint(0, len(balls_surf)-1)
    x = randint(20, W-20)
    speed = randint(1, 4)
    return Ball(x, speed, balls_surf[indx], balls_data[indx]['score'], group)

game_score = 0

def collideBalls():
    global game_score
    for ball in balls:
        if t_rect.collidepoint(ball.rect.center):
            game_score += ball.score
            ball.kill()

balls = pygame.sprite.Group()

speed = 10 #скорость движения обьекта

# b1 = Ball(W//2-250, speed, 'sprites/balls/ball1.png')  # обьект - мячь, импортирован с другого файла, принимает расположение по координате х и путь к файлу
# b2 = Ball(W//2, speed+6, 'sprites/balls/ball2.png')
# b3 = Ball(W//2+350, speed-2, 'sprites/balls/ball3.png')
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# balls.add(Ball(W//2-250, speed, 'sprites/balls/ball1.png'), # добавляем и группу обьекты
#           Ball(W//2, speed+6, 'sprites/balls/ball2.png'),
#           Ball(W//2+350, speed-2, 'sprites/balls/ball3.png'))

createBall(balls)

while True:
    for event in pygame.event.get():  #следит за всеми событиями которые проимходят в окне
        if event.type == pygame.QUIT: #если польз нажимает выход
            exit() #выходит из программы
        elif event.type == pygame.USEREVENT:
            createBall((balls))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        t_rect.x -= speed
        if t_rect.x < 0:
            t_rect.x = 0
    elif keys[pygame.K_RIGHT]:
        t_rect.x += speed
        if t_rect.x > W-t_rect.width:
            t_rect.x = W-t_rect.width

    collideBalls()

    sc.blit(bg, (0, 0)) #отображаем фон
    # sc.blit(b1.image, b1.rect) #отображаем обьект
    # sc.blit(b2.image, b2.rect)
    # sc.blit(b3.image, b3.rect)
    sc.blit(score, (0, 0))
    sc_text = f.render(str(game_score), 1, (94, 138, 14))
    sc.blit(sc_text, (13, 3))

    balls.draw(sc)# прорисовываем группу обьектов в плоскости sc
    sc.blit(telega, t_rect)

    pygame.display.update() #обновляем главн окно

    clock.tick(FPS) #60кадров в секунду

    balls.update(H)

    # # это отвечает за перемещение нашего спрайта и его лучше написать в самом спрайте где она создана
    # if b1.rect.y < H-20:  #проверяем если обьект по у координате меньше чем высота-20
    #     b1.rect.y += speed #тогда добавляем скорость то есть движется по у вниз
    # else:  #а если нет
    #     b1.rect.y = 0 #обнуляем по коорд у
