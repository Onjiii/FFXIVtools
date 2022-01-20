import math
import itertools

def Main():
    Geartest = Gearset_Fending(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
    print(Geartest.AllowedMelds)
    AllMeldCombs = Xmeld(Geartest.AllowedMelds)


class Gearslot():
    def __init__(self):
        self.Head = None
        self.Chest = None
        self.Hands = None
        self.Legs = None
        self.Feet = None
        self.Ear = None
        self.Neck = None
        self.Bracelet = None
        self.Ring1 = None
        self.Ring2 = None

class Gearset_Fending():

    def __init__(self, Weapon, Head, Chest, Hands, Legs, Feet, Ear, Neck, Bracelet, Ring1, Ring2):
        self.Gearslot = Gearslot()

        SlotSetup = {'CRIT':0, 'DET':0, 'DH':0, 'SKS':0, 'SPS':0, 'TEN':0, 'PIE':0}
        self.AllowedMelds = [SlotSetup, SlotSetup, SlotSetup, SlotSetup, SlotSetup, SlotSetup, 
                            SlotSetup, SlotSetup, SlotSetup, SlotSetup, SlotSetup]

        self.Strength = 0
        self.Dexterity = 0
        self.Vitality = 0
        self.Intelligence = 0
        self.Mind = 0
        self.CriticalHit = 0
        self.Determination = 0
        self.DirectHitRate = 0
        self.Defense = 0
        self.MagicDefense = 0
        self.AttackPower = 0
        self.SkillSpeed = 0
        self.AttackMagicPotency = 0
        self.HealingMagicPotency = 0
        self.SpellSpeed = 0
        self.Tenacity = 0
        self.Piety = 0

        match Weapon:
            case 1:
                print('Weapon no 1 chosen')                
            case 2:
                print('Weapon no 2 chosen')

        match Head:
            case 1:
                print('Head no 1 chosen')
                self.Gearslot.Head = "Radiant's Helm of Fending"
                print(self.AllowedMelds[1])
                self.AllowedMelds[1].update({'CRIT':0, 'DET':2, 'DH':2, 'SKS':1, 'SPS':0, 'TEN':2, 'PIE':0})
                self.Strength += 170
                self.Vitality += 176
                self.CriticalHit += 158
                self.SkillSpeed += 111
            case 2:
                print('Head no 2 chosen')

        match Chest:
            case 1:
                print('Chest no 1 chosen')
            case 2:
                print('Chest no 2 chosen')

        match Hands:
            case 1:
                print('Hands no 1 chosen')
            case 2:
                print('Hands no 2 chosen')

        match Legs:
            case 1:
                print('Legs no 1 chosen')
            case 2:
                print('Legs no 2 chosen')

        match Feet:
            case 1:
                print('Feet no 1 chosen')
            case 2:
                print('Feet no 2 chosen')

        match Ear:
            case 1:
                print('Ear no 1 chosen')
            case 2:
                print('Ear no 2 chosen')

        match Neck:
            case 1:
                print('Neck no 1 chosen')
            case 2:
                print('Neck no 2 chosen')

        match Bracelet:
            case 1:
                print('Bracelet no 1 chosen')
            case 2:
                print('Bracelet no 2 chosen')

        match Ring1:
            case 1:
                print('Ring no 1 chosen')
            case 2:
                print('Ring no 2 chosen')

        match Ring2:
            case 1:
                print('Ring no 1 chosen')
            case 2:
                print('Ring no 2 chosen')



class MeldStats():
    def __init__(self, CRIT, DET, DH, SKS, SPS, TEN, PIE):
        self.CriticalHit = CRIT * 36
        self.Determination = DET * 36
        self.DirectHitRate = DH * 36
        self.SkillSpeed = SKS * 36
        self.SpellSpeed = SPS * 36
        self.Tenacity = TEN * 36
        self.Piety = PIE * 36

    def show(self):
        pass



def Xmeld(allowance):
    SlotRange = []
    for MeldSet in allowance:
        for k in MeldSet.values():
            SlotRange.append(list(range(0, k + 1)))
    AllCombinations = list(itertools.product(*SlotRange))

    AllowedCombinations = []
    for index, meldSet in enumerate(AllCombinations):
        if sum(meldSet) == 2:
            AllowedCombinations.append(meldSet)

    return AllowedCombinations




if __name__ == "__main__":
    Main()
