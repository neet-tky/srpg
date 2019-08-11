import numpy as np
import math
import random

class HitCalc(object):
    def __init__(self):
        self.correction = 1.
        self.avoid_corr = 1.
        self.ace = 0

        self.size = 1
        self.map_geo = 1.1

    def __call__(self, atk, _def):
        basichit = self.basichit(atk)
        basicavoid = self.basicavoid(_def)
        calchit = self.calchit(basichit, basicavoid)
        print(self.finalhit(calchit))
        return self.finalhit(calchit)

    def basichit(self, atk):
        return (atk["hit"] / 2 + atk["MOBILE"]) * atk["map_geo"] + atk["w_hit"]

    def basicavoid(self, _def):
        return (_def["avoid"] / 2 + _def["MOBILE"]) * _def["map_geo"]

    def calchit(self, hit, avoid, ):
        return (hit - avoid) * self.size + self.map_geo

    def finalhit(self, calchit):
        return (calchit + self.correction) * self.avoid_corr + self.ace

class DamageCalc(object):
    def __init__(self):
        super(DamageCalc, self).__init__()
        self.map_geo = 1
        self.atk = 300
        self._def = 200
        self.sa = 1
        self.mind = 1

    def __call__(self, atk, _def):
        attack = self.basicattack(atk["w_atk"], atk["geo"])
        defence = self.basicdefence(_def["ARMOR"], atk["geo"])
        return self.finaldamege(attack, defence)

    def basicattack(self, weapon, geo):
        return weapon * self.atk / 200 * geo

    def basicdefence(self, armor, geo):
        return armor * self._def / 200 * geo

    def finaldamege(self, attack, defence):
        return (attack - defence) * self.map_geo * self.sa * self.mind

class Battle(object):
    def __init__(self):
        self.hitcalc = HitCalc()
        self.damagecalc = DamageCalc()

    def __call__(self, atk, _def):
        damage, hit = self.damage(atk, _def)
        remaining_def_HP = _def["HP"] - damage if _def["HP"] > damage else 0

        if _def["counter"]:
            counter_damage, counter_hit = self.damage(_def, atk)
            remaining_atk_HP = atk["HP"] - counter_damage if atk["HP"] > counter_damage else 0
            return {"atk_hp": remaining_atk_HP, "def_hp": remaining_def_HP, "atk_hit": hit, "def_hit": counter_hit}

        return {"atk_hp": atk["HP"], "def_hp": remaining_def_HP, "atk_hit": hit, "def_hit": "-"}

    def damage(self, atk, _def):
        prob = random.randint(0, 100)
        hit = self.hitcalc(atk, _def)
        result_damage = self.damagecalc(atk, _def) if prob <= hit else 0
        return result_damage, hit

if __name__ == '__main__':
    atk = {"hit": 400, "avoid": 300, "geo": 1.1, "map_geo": 1.1,
           "HP": 4500, "ARMOR": 1450, "MOBILE": 120,
           "w_atk": 3500, "w_hit": 30, "w_geo": 1.0}

    _def = { "hit": 300, "avoid": 300, "geo": 1.1, "map_geo": 1.1,
             "HP": 4500, "ARMOR": 1450, "MOBILE": 120,
             "w_atk": 3700, "w_hit": 30, "w_geo": 1.0, "counter":True}

    battle = Battle()
    atk["HP"], _def["HP"] = battle(atk, _def)
    print(atk["HP"], _def["HP"])



