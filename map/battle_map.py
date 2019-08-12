import pygame
from pygame.locals import *
import sys

import random

mapDB = {
"part1":[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
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
}

img_DB = {
    "map" : {"0": "figure/grass.png", "1": "figure/water.png" },
    "enemy": { "unko1": "figure/enemy.png", "unko2": "figure/enemy.png", "unko3": "figure/enemy.png", "unko4": "figure/enemy.png", "unko5": "figure/enemy.png" },
    "own" : { "thi": "figure/mikata.png" },
    "select": "figure/select.png"
}

class RobotLocate(object):
    def __init__(self, img_DB, screen):
        self.own_db = loads_imgs(img_DB["own"])
        self.enemy_db = loads_imgs(img_DB["enemy"])

        self.enemy_locate = {}
        self.own_locate = {}
        self.msize = 32
        self.screen = screen

    def __call__(self, *args, **kwargs):
        self.enemy_locate = self._disp_robot(self.enemy_db)
        self.own_locate = self._disp_robot(self.own_db)

        return {"enemy": self.enemy_locate, "own": self.own_locate}

    def _disp_robot(self, imgs):
        locate_db = {}

        for key, img in imgs.items():
            x_axis = random.randint(0, 14) * self.msize
            y_axis = random.randint(0, 14) * self.msize
            self.screen.blit(img, (x_axis, y_axis))
            locate_db[str(key)] = Rect(x_axis, y_axis, self.msize, self.msize)

        return locate_db

class MAP(object):
    def __init__(self, map_data, img_DB, screen):
        self.map = map_data
        self.row = len(self.map)
        self.col = len(self.map[0])

        self.msize = 32

        self.map_db = loads_imgs(img_DB["map"])
        self.select_db = {}
        self.select_db["serif"] = load_img(img_DB["select"], (800, 120))
        self.select_db["select"] = load_img(img_DB["select"], (160, 480))
        self.screen = screen

    def __call__(self):
        self.screen.blit(self.select_db["select"], (640, 0))
        self.screen.blit(self.select_db["serif"], (0, 480))

        for y in range(self.row):
            for x in range(self.col):
                self.screen.blit(self.map_db[str(self.map[y][x])], (x * self.msize, y * self.msize))

class DisplayMAP(object):
    SIZE = (800, 600)

    def __init__(self, mapdb, imgdb):
        pygame.init()
        self.screen = pygame.display.set_mode(self.SIZE)

        self.map = MAP(mapdb, imgdb, self.screen)
        self.robot_locate = RobotLocate(imgdb, self.screen)
        self.action_select = ActionSelect()
        self.running = True

        self.locate = {}

    def __call__(self, *args, **kwargs):
        self.map()
        self.locate = self.robot_locate()
        print(self.locate)
        while self.running:
            self.drawupdate()
            self.events()

    def drawupdate(self):
        pygame.display.update()

    def events(self):
        for event in pygame.event.get():
            self._finishevents(event)
            self._clickedevents(event)

    def _finishevents(self, event):
        if event.type == QUIT:
            self.running = False
            pygame.quit()
            sys.exit()

    def _clickedevents(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for key, own_locate in self.locate["own"].items():
                if own_locate.collidepoint(event.pos):
                    print("own robot was pressed")


def load_img(file, size=(32, 32)):
    img = pygame.image.load(file).convert_alpha()
    colorkey = img.get_at((0, 0))
    img.set_colorkey(colorkey, RLEACCEL)
    return pygame.transform.scale(img, size)

def loads_imgs(names, size=(32, 32)):
    imgs = {}
    for k, v in names.items():
        imgs[k] = load_img(v, size)

    return imgs

if __name__=="__main__":
    maps = DisplayMAP(mapDB["part1"], img_DB)
    maps()
