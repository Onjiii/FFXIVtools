

def Main():
    Onji = Character(Level = 90,
                     Strength=0,
                     Dexterity=0,
                     Vitality=0,
                     Intelligence=0,
                     Mind=0,
                     CriticalHit=0,
                     Determination=0,
                     DirectHitRate=0,
                     Defense=0,
                     MagicDefense=0,
                     AttackPower=0,
                     SkillSpeed=0,
                     AttackMagicPotency=0,
                     HealingMagicPotency=0,
                     SpellSpeed=0,
                     Tenacity=0,
                     Piety=0)

    print(Onji.Level)


class Attributes():
    def __init__(self, Strength, Dexterity, Vitality, Intelligence, Mind):
        self.Strength = Strength
        self.Dexterity = Dexterity
        self.Vitality = Vitality
        self.Intelligence = Intelligence
        self.Mind = Mind


class Offensive():
    def __init__(self, CriticalHit, Determination, DirectHitRate):
        self.CriticalHit = CriticalHit
        self.Determination = Determination
        self.DirectHitRate = DirectHitRate


class Defensive():
    def __init__(self, Defense, MagicDefense):
        self.Defense = Defense
        self.MagicDefense = MagicDefense


class Physical():
    def __init__(self, AttackPower, SkillSpeed):
        self.AttackPower = AttackPower
        self.SkillSpeed = SkillSpeed


class Mental():
    def __init__(self, AttackMagicPotency, HealingMagicPotency, SpellSpeed):
        self.AttackMagicPotency = AttackMagicPotency
        self.HealingMagicPotency = HealingMagicPotency
        self.SpellSpeed = SpellSpeed

class Role():
    def __init__(self, Tenacity, Piety):
        self.Tenacity = Tenacity
        self.Piety = Piety


class Character_sub():
    def __init__(self,Level, Strength, Dexterity, Vitality, Intelligence, Mind, CriticalHit,
                 Determination, DirectHitRate, Defense, MagicDefense, AttackPower, SkillSpeed,
                 AttackMagicPotency, HealingMagicPotency, SpellSpeed, Tenacity, Piety):
        self.Level = Level
        self.Attributes = Attributes(Strength, Dexterity, Vitality, Intelligence, Mind)
        self.Offensive = Offensive(CriticalHit, Determination, DirectHitRate)
        self.Defensive = Defensive(Defense, MagicDefense)
        self.Physical = Physical(AttackPower, SkillSpeed)
        self.Mental = Mental(AttackMagicPotency, HealingMagicPotency, SpellSpeed)
        self.Role = Role(Tenacity, Piety)


class Character():
    def __init__(self,Level, Strength, Dexterity, Vitality, Intelligence, Mind, CriticalHit,
                 Determination, DirectHitRate, Defense, MagicDefense, AttackPower, SkillSpeed,
                 AttackMagicPotency, HealingMagicPotency, SpellSpeed, Tenacity, Piety):
        self.Level = Level
        self.Strength = Strength
        self.Dexterity = Dexterity
        self.Vitality = Vitality
        self.Intelligence = Intelligence
        self.Mind = Mind
        self.CriticalHit = CriticalHit
        self.Determination = Determination
        self.DirectHitRate = DirectHitRate
        self.Defense = Defense
        self.MagicDefense = MagicDefense
        self.AttackPower = AttackPower
        self.SkillSpeed = SkillSpeed
        self.AttackMagicPotency = AttackMagicPotency
        self.HealingMagicPotency = HealingMagicPotency
        self.SpellSpeed = SpellSpeed
        self.Tenacity = Tenacity
        self.Piety = Piety



if __name__ == "__main__":
    Main()
