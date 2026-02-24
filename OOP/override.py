# override :gampangane kyok nimpa/genti method teko superclass ngo sub class
# syarate kudu podo plek jengan method e 


class Hero:

    def __init__(self,name,health):
        self.name = name
        self.health = health

    def info(self):
        print("Halo dari Hero")
        print(f"{self.name} Health : {self.health}")

class Hero_pisikal(Hero):
    def __init__(self,name):
        super().__init__(name,100)
    # override
    def info(self):
        print(f"{self.name} dengan tipe : pisikal, health : {self.health}")

class Hero_majik(Hero):
    def __init__(self,name):
        super().__init__(name,50)

alu = Hero_pisikal("Alu")
selena = Hero_majik("Selena")

alu.info() #iki gowo method seng nek njero sub class
selena.info() #iki nggowo seng nek super class e