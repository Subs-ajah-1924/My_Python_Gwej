# inheritance : intine class seng ndue keturunan
# intine iso ngenggo atribut/method seng nek njero super class e

# jengene Super class 
class Hero:

    def __init__(self,name,health):
        self.name = name
        self.health = health
        # print(f"Halo {self.name}")

    def info(self):
        print(f"{self.name} dengan hp : {self.health}")

    def yaya(self):
        print("bruhhh")

# jengene Sub class
class HeroMagic(Hero): #corone iku sub class e kei kurong,trs kurunge iku wei jengen super class e

    def __init__(self,name):
        super().__init__(name,100) #super iki merujuk ke super class e
        super().info() # iki contone gowo super(),gak usah genti genti jengen class e misal class e di genti jengene
        Hero.info(self) # tek nggowo iki pomo jengen class e berubah,y harus di ubah podo

    def sapa(self):
        print(f"Halo {self.name}")


selena = HeroMagic("Selena")
selena.sapa()
selena.yaya()

