import pygame
from pygame.locals import *
import sys
import random

map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

enemy_imgname = "figure/enemy.png"
mikata_imgname = "figure/mikata.png"
grass_imgname = "figure/grass.png"
water_imgname = "figure/water.png"
w_select_img = "figure/select.png"

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

row = len(map)
col = len(map[0])
imgs = [None] * 256

msize = 32
runnning = True

SIZE = (800, 600)
map_size = Rect(0, 0, 640, 480)
command_size = Rect(640, 0, 160, 480)
screen_size = Rect(0, 480, 80, 120)
# main
pygame.init()
screen = pygame.display.set_mode(SIZE)

def load_img(file):
    img = pygame.image.load(file).convert_alpha()
    colorkey = img.get_at((0, 0))
    img.set_colorkey(colorkey, RLEACCEL)
    return img

def _disp_frame():

    screen.blit(imgs[2], (640, 0))
    screen.blit(imgs[3], (0, 480))
    for y in range(row):
        for x in range(col):
            screen.blit(imgs[map[y][x]], (x * msize, y * msize))

def _disp_enemy():
    db = {}
    for num in range(10):
        print(num)
        x_axis = random.randint(0, 14)
        y_axis = random.randint(0, 14)
        screen.blit(imgs[4], (x_axis*msize, y_axis*msize))
        db[str(num)] = Rect(x_axis*msize, y_axis*msize, msize, msize)
    return db

def _disp_own():
    db = {}
    x_axis = random.randint(0, 19)
    y_axis = random.randint(0, 19)
    screen.blit(imgs[5], (x_axis*msize, y_axis*msize))
    db[str(0)] = Rect(x_axis*msize, y_axis*msize, msize, msize)
    return db


def load_img(file):
    return pygame.image.load(file).convert()

imgs[0] = load_img(grass_imgname)
imgs[1] = load_img(water_imgname)

imgs[2] = load_img(w_select_img)
imgs[2] = pygame.transform.scale(imgs[2], (160, 480))

imgs[3] = load_img(w_select_img)
imgs[3] = pygame.transform.scale(imgs[3], (800, 120))
imgs[4] = load_img(enemy_imgname)
imgs[4] = pygame.transform.scale(imgs[4], (msize, msize))

imgs[5] = load_img(mikata_imgname)
imgs[5] = pygame.transform.scale(imgs[5], (msize, msize))

_disp_frame()
enemy_locate_db = _disp_enemy()
own_locate_db = _disp_own()
pygame.display.update()
print(enemy_locate_db)
print(own_locate_db)
while runnning:
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            runnning = False
            pygame.quit()
            sys.exit()

