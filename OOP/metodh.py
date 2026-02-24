class Hero:
    jumlah_hero = 0

    def __init__(self, name,health,power,armor):
        self.name = name
        self.health = health
        self.power = power
        self.armor = armor
        Hero.jumlah_hero += 1

    # metodh tanpa return
    def hay(self):
        print(f"My Namaku adalah {self.name}")

    def regen(self,nilai_regen):
        self.health += nilai_regen #misal iki ono return e gak iso ngenggo "=" mergo iki nggawe variabel nek njero return e

    def nyowone(self):
        return self.health

hero_1 = Hero("Yin",1000,9999,12)
hero_2 = Hero("Suyu",1000,7532,88)

print(hero_1.__dict__)
print(hero_2.__dict__)

hero_1.hay()
print(hero_2.regen())
print(hero_2.nyowone())