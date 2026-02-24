class Hero:

    def __init__(self,name,health,armor):
        self.name = name
        self.__health = health
        self.__armor = armor

        # self.info = "name {} \n\t health ={}".format(self.name,self.__health) //iki pomo namane mbok genti y tetep ngenggo nama ne objek e,gak iso ke update

    @property # iki gampangane nganggep method iku koyok variabel,dadi manggile y gak usah nggowo kurung neh "()"
    def info(self): 
        # iki tek pengen ke update trs pomo pengen nggenti nggenti hal senng mbok lebokno string 
        return "name : {} \n\t health ={}".format(self.name,self.__health)
    
    # gawe getter/setter/deleter kanggo armor
    @property
    def armor(self):
        pass
    
    # getter
    @armor.getter
    def armor(self):
        return self.__armor
    
    # setter
    @armor.setter
    def armor(self,input):
        self.__armor = input
    
    # deleter
    @armor.deleter
    def armor(self):
        print("armor telah di hapus")
        self.__armor = None

alu = Hero("Alu",200,10)

print("Mengubah info")
print(alu.info)
alu.name = 'Miya'
print(alu.info)

print("========")
print("get")
print(alu.armor)

print("========")
print("set")
alu.armor = 40
print(alu.armor)

print("========")
del alu.armor
print(alu.__dict__)