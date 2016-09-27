
class Monster:
    def __init__(self):
        self.hp = 10


class Weapon:

    def __init__(self):
        self.damage = 0
        self.durability = 0

    def attack(self):  # external method
        self.set_durability()  # internal method
        return self.damage

    def set_durability(self):
        self.durability -= 1
        if self.durability <= 0:
            self.durability = 0
            self.damage = 0


class Sword(Weapon):

    def __init__(self):
        self.damage = 3
        self.durability = 10


class UnbreakableSword(Sword):

    def set_durability(self):
        pass

orc = Monster()
bad_sword = Weapon()
ok_sword = Sword()

orc.hp -= ok_sword.attack()
print (orc.hp)
