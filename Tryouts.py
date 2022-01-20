

def Main():
    p, f = CriticalHit(1000)
    print(p, f)



def LevelLv(Lvl):
    SUB = [341, 354, 364, 380, 400][[50, 60, 70, 80, 90].index(Lvl)]
    DIV = [341, 600, 900, 1300, 1900][[50, 60, 70, 80, 90].index(Lvl)]
    return SUB, DIV

def CriticalHit(CRIT, Level=90):
    SUB, DIV = LevelLv(Level)
    pCRIT = ((200*(CRIT - SUB)/DIV) + 50)/10
    fCRIT = 1400 + (200*(CRIT - SUB)/DIV)

    return pCRIT, fCRIT

if __name__ == "__main__":
    Main()
