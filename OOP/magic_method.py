# magic method,di tandai dengan 2 underscore di d epan dan di belakang

class Pelem:
    
    # iki misal si class e di sebut,nko program pertama seng jalan iki
    def __init__(self,nama,jumlah):
        self.nama = nama
        self.jumlah = jumlah

    # iki gampangane kyok cadangan misal kwe ngeprin objek e tanpo method opo opo
    def __str__(self):
        return f"Objek ini bernama {self.nama} dengan jumlah {self.jumlah}"
    
    # iki podo seng __str__,cuman bedane iki kyok pengen ngedebug nggowone iki.
    # pomo ono __str__ y seng ke print str e.coro manuale nggowo ngene print(repr(objek))
    def __repr__(self):
        return f"Objek ini bernama {self.nama} dengan jumlah {self.jumlah}"
    
    #iki pomo ono parameter "+",nko kepanggil
    def __add__(self,objek):
        return self.jumlah + objek.jumlah
    
    # magic method podo iso di override,conto
    @property #kudu nggowo iki,ben manggile gasah nggo kurung "()"
    def __dict__(self):
        return "Objek ini memiliki Nama dan Jumlah"
    

pelem1 = Pelem("Manalagi",10)
pelem2 = Pelem("Gadong",100)

# jajal seng str
print(pelem1)
print(repr(pelem2))
print(pelem1 + pelem2)
print(pelem1.__dict__)