

def Main():
    test = Player()
    print(test.fDET)


class Equipped():
    def __init__(self, Character, Gear, Melds):
        pass

def Damage(Potency, DET, AP):
    fDET = Determination(DET)
    fAP = AttackPower(AP)
    Damage = (((Potency * fDET * fAP) / 100) / 1000)
    return Damage


def LevelLv(Lvl):
    MAIN = [202, 218, 292, 340, 390][[50, 60, 70, 80, 90].index(Lvl)]
    SUB = [341, 354, 364, 380, 400][[50, 60, 70, 80, 90].index(Lvl)]
    DIV = [341, 600, 900, 1300, 1900][[50, 60, 70, 80, 90].index(Lvl)]
    return MAIN, SUB, DIV


def JobModifier(key):
    JobMods = {'PLD': 100, 'WAR': 105, 'DRK': 105, 'GNB': 100}
    Mod = JobMods[key]
    return Mod


def Determination(DET, Level=90):
    MAIN, SUB, DIV = LevelLv(Level)
    fDET = (130*(DET - MAIN) / DIV + 1000)
    return fDET


def CriticalHit(CRIT, Level=90):
    MAIN, SUB, DIV = LevelLv(Level)
    pCRIT = ((200*(CRIT - SUB)/DIV) + 50)/10
    fCRIT = 1400 + (200*(CRIT - SUB)/DIV)
    return fCRIT, pCRIT


def DirectHit(DH, Level=90):
    MAIN, SUB, DIV = LevelLv(Level)
    fDH = 0
    pDH = (550*(DH - SUB)/DIV) / 10
    return fDH, pDH


def Tenacity(TEN, Level=90):
    MAIN, SUB, DIV = LevelLv(Level)
    fTEN = 100 * (TEN - SUB) / DIV + 1000
    return fTEN


def Speed(SPD, Level=90):
    MAIN, SUB, DIV = LevelLv(Level)
    fSPD = 130 * (SPD - SUB) / DIV + 1000
    return fSPD


def AutoAttack(Job, WD, Wdelay):
    MAIN, SUB, DIV = LevelLv(Level)
    JobMod = JobModifier(Job)
    fAUTO = ((MAIN * JobMod / 1000) + WD) * (Wdelay / 3)
    return fAUTO


def WeaponDamage(Job, WD, Level=90):
    MAIN, SUB, DIV = LevelLv(Level)
    fWD = ((MAIN * JobMod(Job) / 1000) + WD)
    return fWD


def AttackPower(AP):
    # fAP = (165  * ( AP - 340 ) / 340 ) + 100 #Non-Tanks Level 80
    fAP = (115 * (AP - 340) / 340) + 100  # Tanks Level 80
    return fAP


def Direct_Damage():
    D1 = ((Potency * fATK * fDET) / 100) / 1000
    D2 = (((((D1 * fTEN) / 1000) * fWD) / 100) * Trait) / 100
    D3 = ((((D2 * modCRIT) / 1000) * modDH) / 100)
    D = ((((D3 * np.randint(95, 105)) / 100) * buff_1) * buff_2)
    return D


def DoT_Damage():
    D1 = (((Potency * fATK * fDET) / 100) / 1000)
    D2 = ((((((((D1 * fTEN) / 1000) * fSPD) / 1000) * fWD) / 100) * Trait) / 100) + 1
    D3 = ((D2 * np.randint(95, 105)) / 100)
    D = ((((((D3 * modCRIT) / 1000) * modDH) / 100) * buff_1) * buff_2)
    return D

def AutoAtk_Damage():
    D1 = (((Potency * fATK * fDET ) /100 ) /1000 )
    D2 = ((((((((D1 * fTEN ) /1000 ) * fSPD ) /1000 )* fAUTO ) /100 ) * Trait ) /100 )
    D3 = ((((D2 * modCRIT ) /1000 ) * modDH ) /100 )
    D = ((((D3 * np.randint(95,105) ) /100 ) * buff_1 ) * buff_2 )
    return D

if __name__ == "__main__":
    Main()
