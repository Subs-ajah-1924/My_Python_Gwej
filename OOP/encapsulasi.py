#aturan encapsulasi:
#1.untuk semua private variable
#2.getter(mengambil variable) and setter(menyetting variable)
# intine kanggo ngurusi variabel private lah,kyok nyimpen,njogo,tah ngubah ngubah(get/set)
class Hero:

    def __init__(self,nama,darah):
        self.__nama = nama
        self.__darah = darah

    # Method Getter
    def get_nama(self):
        return self.__nama
    
    def get_darah(self):
        return self.__darah
    
    # Metodh setter
    def set_hp(self,sisa_nyawa):
        if sisa_nyawa > 0:
            self.__darah = sisa_nyawa
        else:
            print("Hero mu sudah mati")

hero_1 = Hero("Alu",200)

print(hero_1.get_nama())
#           |method get|
print(hero_1.get_darah())
#           |method get|

hero_1.set_hp(29)
print(hero_1.get_darah()) #iki hasile seng nduwur
#     |metodh set|
hero_1.set_hp(-2) # hasile y else iki
#     |metodh set|