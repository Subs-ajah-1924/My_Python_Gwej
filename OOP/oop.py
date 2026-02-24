class Hero: #Template
    # class variabel = variabel seng ono nek njero class e
    jumlah = 0

    def __init__(self,name,health,power,armor):
        # instance variable = variabel seng ono nek njero def
        self.name = name 
        self.health = health
        self.power = power
        self.armor = armor
        Hero.jumlah += 1

hero_1 = Hero("Alu",1000,999999,2)
hero_2 = Hero("Miya",1000,254,2)
hero_3 = Hero("Ya",1000,23,2)
print()


print(hero_1.__dict__) #kanggo ndelok komponen e


