class Hero:


    def __init__(self,name,health,pysical_damage,armor,items):
        self.name = name
        self.health = health
        self.pysical_damage = pysical_damage
        self.armor = armor
        self.items = items

        if self.items == "BOD":
            self.pysical_damage += 100
        elif self.items == "windtalker":
            self.pysical_damage += 70

    def nyerang(self,musuh):
        print(F"{self.name} Menyerang {musuh.name}")
        demeg =(self.pysical_damage / musuh.armor)
        musuh.diserang(self,demeg)

    def diserang(self,musuh,attack_powe_musoh):
        print(f"\n{self.name} diserang {musuh.name}")
        print(f"dengan damage \t= {round(attack_powe_musoh)}")
        sisa_nyowo = self.health - attack_powe_musoh
        print(f"Sisa nyawa \t= {round(sisa_nyowo)}")


alu = Hero("alu",1000,100,3,"BOD")
miya = Hero("miya",500,100,3,"windtalker")

alu.nyerang(miya)
