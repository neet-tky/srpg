from damage import battle

if __name__ == '__main__':
    atk = {"name":"name", "hit": 400, "avoid": 300, "geo": 1.1, "map_geo": 1.1,
           "HP": 4500, "EN": 200, "ARMOR": 1450, "MOBILE": 120,
           "weapon":"w_name", "w_atk": 3500, "w_hit": 30, "w_geo": 1.0}

    atk = {"name":"name", "hit": 400, "avoid": 300, "geo": 1.1, "map_geo": 1.1,
           "HP": 4500, "EN": 200, "ARMOR": 1450, "MOBILE": 120,
           "weapon":"w_name", "w_atk": 3500, "w_hit": 30, "w_geo": 1.0}

    bcalc = battle.Battle()
    atk["HP"], _def["HP"] = bcalc(atk, _def)
    print(atk["HP"], _def["HP"])
