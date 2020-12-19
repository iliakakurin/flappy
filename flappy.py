# здесь подключаются модули
import pygame
import sys
from player_flappy import *
from obstacle_flappy import *

def intersects(o):
    global pl
    x = o.x
    y = o.h
    if (pl.x - x)**2 + (pl.y - y)**2 <= pl.r**2:
        return True
    x = o.x
    y = o.h + o.gap
    if (pl.x - x)**2 + (pl.y - y)**2 <= pl.r**2:
        return True
    return False

# здесь определяются константы,
# классы и функции
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)

# здесь происходит инициация,
# создание объектов
width = 600
height = 400
pygame.init()
sc = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
vy = 0
vx_o = -1
time = 0
score = 0

# если надо до цикла отобразить
# какие-то объекты, обновляем экран
pygame.display.update()

pl = Player(width, height, PINK)
ob = []
o = Obstacle(width, height, LIGHT_BLUE)
ob.append(o)
# главный цикл
while True:

    # задержка
    time += 1
    score += 1
    clock.tick(FPS)
    sc.fill(WHITE)
    # цикл обработки событий

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
        if i.type == pygame.KEYDOWN:
            print(i)
            if i.key == 1073741905:
                vy = 2
                print(i)
            elif i.key == 1073741906:
                vy = -2
                print(i)
        if i.type == pygame.KEYUP:
            vy = 0


    # --------
    # изменение объектов
    # --------
    # передвигаем объекты
    if time % 200 == 0:
        o = Obstacle(width, height, LIGHT_BLUE)
        ob.append(o)
    pl.y += vy
    for obs in ob:
        obs.x += vx_o
        if obs.x + obs.w <= 0:
            ob.remove(obs)

    for obs in ob:
        if intersects(obs):
            print('GAME OVER! YOU DIE!')
            print('Your score:', score)
            sys.exit()


    # обновление экрана
    for obs in ob:
        pygame.draw.rect(sc, obs.color, (obs.x, 0, obs.w, obs.h))
        pygame.draw.rect(sc, obs.color, (obs.x, obs.h + obs.gap, obs.w, height - obs.h - obs.gap))
    pygame.draw.circle(sc, pl.color, (pl.x, pl.y), pl.r)
    pygame.display.update()


