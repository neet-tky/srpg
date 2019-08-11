import math



if __name__=='__main__':
    Dcalc = DamageCalc()
    atk = {"weapon": 4000, "geo": 1.0}
    _def = {"armor": 1450, "geo": 1.1}

    dam = Dcalc(atk, _def)
    print(dam)

