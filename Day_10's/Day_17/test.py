class Weapon:
    def __init__(self):
        self.damage = 100

    def attack(self):
        print(f"l'arme inflige {self.damage} dégats")


class Player:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def attack(self):
        print(f"l'arme inflige {self.damage} degats")
    
    def attack_enemy(self):
        print(f"{self.name} attaque!!")
        self.attack()

arme_1 = Weapon()
arme_1.attack()
print(arme_1.damage)

arme_1 = Weapon()
player_1 = Player("Google", arme_1)
player_1.attack_enemy()
print(player_1)
    