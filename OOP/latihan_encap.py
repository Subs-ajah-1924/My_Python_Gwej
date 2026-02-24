class Hero:

    __jumlah = 0

    def __init__(self,name,health,att,armor):
        self.__name = name
        self.__healthstandar = health
        self.__attstandar = att
        self.__armorstandar = armor
        self.__level = 1
        self.__exp = 0

        self.__maxhp = self.__healthstandar * self.__level
        self.__maxatt = self.__attstandar * self.__level
        self.__armor = self.__armorstandar * self.__level

        self.__health = self.__maxhp
        Hero.__jumlah += 1

    @property
    def info(self):
        return "{} level {}: \n\thealth : {}/{} \n\tatt : {} \n\tarmor : {}".format(self.__name,self.__level,self.__health,self.__maxhp,self.__maxatt,self.__armor)
    
    @property
    def gainexp(self):
        return self.__exp

    @gainexp.setter
    def gainexp(self,addexp):
        self.__exp += addexp
        print(f"{self.__name} mendapatkan exp = {addexp}\n")
        while self.__exp >= 100:
            if self.__exp >= 100:
                print(f"{self.__name} Level Up!")
                self.__level += 1
                self.__exp -= 100

                self.__maxhp = self.__healthstandar * self.__level
                self.__maxatt = self.__attstandar * self.__level
                self.__armor = self.__armorstandar * self.__level

    def attack(self,enemy):
        damage = self.__maxatt / (enemy.__armor / 3)
        print(f"{self.__name} menyerang {enemy.__name}")
        enemy.di_serang(self,damage)
        self.gainexp = 240

    def di_serang(self,musoh,damage):
        self.__health -= damage
        print(f"{self.__name} di serang {musoh.__name}")
        if self.__health >= 0:
            print(f"Nyawa {self.__name} tersisa {self.__health}")
        else:
            print(f"{self.__name} mati.")
            self.__health = 0

alu = Hero("Alu",100,200,10)
miya = Hero("Miya",1000,200,10)

alu.attack(miya)
alu.attack(miya)
alu.attack(miya)
print("")
print(alu.info)
print(alu.gainexp)
