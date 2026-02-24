class Elemen:

    def set_elemen(self,elemen):
        self.elemen = elemen
    
    def show_elemen(self):
        print(f"Elemen {self.elemen}")

    def show(self,nomor):
        print(f"Halo dari Class elemen {nomor}")

class Kelamin:

    def set_kelamin(self,kelamin):
        self.kelamin = kelamin

    def show_kelamin(self):
        print(f"Kelamin {self.kelamin}")

    def show(self,nomor):
        print(f"Halo dari Class Kelamin nomor {nomor}")

class Pokemon(Elemen,Kelamin): # iki iso langsong di wei 2 super class nek siji sub class
    
    def __init__(self,name,health):
        self.name = name
        self.health = health

pikachu = Pokemon("Pikachu",100)
pikachu.set_elemen("Petir")
pikachu.set_kelamin("Waifu")

pikachu.show_elemen()
pikachu.show_kelamin()
pikachu.show(10)
pikachu.show(12)




