import pygame
from pygame.locals import *
import sys
import battle

class DisplayWindow(object):
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    SIZE = (640, 480)

    attack_start = Rect(270, 315, 100, 20)
    command_mind = Rect(270, 339, 100, 20)

    def __init__(self, atk, _def, damage):
        pygame.init()
        pygame.display.set_caption("Battle Screen")

        self.screen = pygame.display.set_mode(self.SIZE)
        self.font = pygame.font.SysFont(None, 14)
        self.font_info = pygame.font.SysFont(None, 25)

        self.running = True

        self.atk = atk
        self._def = _def
        self.damage = damage

    def __call__(self, *args, **kwargs):
        while self.running:
            self.dispBG()
            self.events()
            self.displayupdate()

    def dispBG(self):
        self.screen.fill(self.WHITE)
        self._disp_frame()
        self._disp_select()
        self._disp_info()

    def _disp_frame(self):
        pygame.draw.rect(self.screen, self.BLACK, Rect(30, 30, 260, 200), 2)
        pygame.draw.rect(self.screen, self.BLACK, Rect(350, 30, 260, 200), 2)
        pygame.draw.rect(self.screen, self.BLACK, Rect(30, 240, 260, 40), 2)
        pygame.draw.rect(self.screen, self.BLACK, Rect(350, 240, 260, 40), 2)
        pygame.draw.rect(self.screen, self.BLACK, Rect(250, 300, 140, 150), 2)

    def _disp_select(self):
        self.screen.blit(self.font.render("attack start", True, self.BLACK), (275, 320))
        pygame.draw.rect(self.screen, self.BLACK, self.attack_start, 1)

        self.screen.blit(self.font.render("command of mind", True, self.BLACK), (275, 344))
        pygame.draw.rect(self.screen, self.BLACK, self.command_mind, 1)

        self.screen.blit(self.font.render("add attack", True, self.BLACK), (275, 368))
        pygame.draw.rect(self.screen, self.BLACK, Rect(270, 363, 100, 20), 1)

        self.screen.blit(self.font.render("-", True, self.BLACK), (275, 392))
        pygame.draw.rect(self.screen, self.BLACK, Rect(270, 387, 100, 20), 1)

        self.screen.blit(self.font.render("-", True, self.BLACK), (275, 416))
        pygame.draw.rect(self.screen, self.BLACK, Rect(270, 411, 100, 20), 1)

    def _disp_info(self):
        self.screen.blit(self.font_info.render("HP/EN: " + str(self.atk["HP"]) + " / " + str(self.atk["EN"]), True, self.BLACK), (50, 50))
        self.screen.blit(self.font_info.render(self.atk["name"], True, self.BLACK), (50, 90))
        self.screen.blit(self.font_info.render(self.atk["weapon"], True, self.BLACK), (50, 130))
        self.screen.blit(self.font_info.render(str(self.damage["atk_hit"]) + "%", True, self.BLACK), (50, 250))

        self.screen.blit(self.font_info.render("HP/EN: " + str(self._def["HP"]) + " / " + str(self._def["EN"]), True, self.BLACK), (370, 50))
        self.screen.blit(self.font_info.render(self._def["name"], True, self.BLACK), (370, 90))
        self.screen.blit(self.font_info.render(self._def["weapon"], True, self.BLACK), (370, 130))
        self.screen.blit(self.font_info.render(str(self.damage["def_hit"]) + "%", True, self.BLACK), (370, 250))

    def events(self):
        for event in pygame.event.get():
            self._clickevents(event)
            self._finishevents(event)

    def _finishevents(self, event):
        if event.type == QUIT:
            self.running = False
            pygame.quit()
            sys.exit()

    def _clickevents(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.attack_start.collidepoint(event.pos):
                print("attack_start was pressed")
            if self.command_mind.collidepoint(event.pos):
                print("command_of_mind was pressed")

    def displayupdate(self):
        pygame.display.update()

if __name__ == '__main__':
    atk = {"name":"name", "hit": 400, "avoid": 300, "geo": 1.1, "map_geo": 1.1,
           "HP": 4500, "EN": 200, "ARMOR": 1450, "MOBILE": 120,
           "weapon":"w_name", "w_atk": 3500, "w_hit": 30, "w_geo": 1.0,
           "counter": False
           }

    _def = {"name":"name", "hit": 400, "avoid": 300, "geo": 1.1, "map_geo": 1.1,
            "HP": 4500, "EN": 200, "ARMOR": 1450, "MOBILE": 120,
            "weapon":"w_name", "w_atk": 3500, "w_hit": 30, "w_geo": 1.0,
            "counter": True
            }

    battle = battle.Battle()
    result_damage = battle(atk, _def)
    # {atk_hp, def_hp, atk_hit, def_hit}

    disp = DisplayWindow(atk, _def, result_damage)
    disp()
