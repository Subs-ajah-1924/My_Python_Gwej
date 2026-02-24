# MRO = Method Resolution Order
# gampangane kyok urutan di jikuk e method semisal ono method seng podo persis
# iki terjadi neng multipel inheritance tok
class Elemen:

    def set_elemen(self,elemen):
        self.elemen = elemen
    
    def show_elemen(self):
        print(f"Elemen {self.elemen}")

    def show(self):
        print(f"Halo dari Class")

class Kelamin:

    def set_kelamin(self,kelamin):
        self.kelamin = kelamin

    def show_kelamin(self):
        print(f"Kelamin {self.kelamin}")

    def show(self):
        print(f"Halo dari Class Kelamin")

class Pokemon(Elemen,Kelamin): #iki di jikuk method seng pertama di inheritance,dadi kejikuk seng elemen
    
    def __init__(self,name,health):
        self.name = name
        self.health = health

pikachu = Pokemon("Pikachu",100)
pikachu.show() #hasil e iki elemen
help(pikachu) #iki tek pengen balek pencet "Q"