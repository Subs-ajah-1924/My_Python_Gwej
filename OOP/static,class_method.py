class Hero:

    __jumlah = 0

    def __init__(self,name):
        self.__name = name
        Hero.__jumlah += 1

    # iki isone kanggo objek tok,mergo nggowo self
    def getJumlah(self):
        return Hero.__jumlah
    
    # iki isone kanggo class tok,mergo rak nggowo self
    def getJumlah1():
        return Hero.__jumlah
    
    # nah carane piye ben iso jipuk 2 karone dengan ssatu method?
    # carane nggowo staticmethod dan classmethod

    @staticmethod # intine iki nemplek ngo kabeh(objek ambek class e)
    def getJumlah2():
        return Hero.__jumlah
    
    # @classmethod intine iki ceto nemplek ngo class e,tapi y iso dinggo ngo objek podo
    def getJumlah3(cls): # iki isi pokok e,sembarang rapopo.nek kene tak isi cls ben penak mocone
        return cls.__jumlah


# ========================================================================
alu = Hero("Alu") # tek iki orak
print(f"{alu.getJumlah()} Hero")
# print(Hero.getJumlah()) // iki pomo di run gowo method iku error dadine
# ========================================================================
print(f"{Hero.getJumlah1()} Hero") # tek iki mok iso class e tok,rak iso ngo objek
# ========================================================================
# staticmethod
print("========= Tambahan Miya ======")
miya = Hero("Miya")

print(f"{miya.getJumlah2()} Hero")
print(f"{Hero.getJumlah2()} Hero")
# ========================================================================
# classmethod
print("========= Tambahan Yin ======")
yin = Hero("Yin")

print(f"{yin.getJumlah2()} Hero")
print(f"{Hero.getJumlah2()} Hero")
# ========================================================================
