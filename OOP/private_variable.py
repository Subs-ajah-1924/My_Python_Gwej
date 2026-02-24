class Hero:

    #class variable
    jumlah = 0
    __privatejumlah = 0

    def __init__(self,name,health):
        self.name = name
        self.health = health

        #variable intance private
        self.__private = "private" #coro nggawe ne nggowo under score 2
        #iki pokok e ojo di ubah mergo di jogo ketat.tek pengen ngubah o y rak iso og

        #protected intence variable
        self._protected = "protected" #coro nggawe ne nggowo under score 1
        #iki ameh podo private,cumak iki orak seketat private.value ne iso di ubah ubah(sebaiknya jangan)


yin = Hero("Yin",100)

print(yin.__dict__)
print(Hero.__dict__)
# print(Hero.__privatejumlah) ngene iki raiso

#coro manggil e seng private
print(yin._Hero__private)
#iki kudu nggowo coro khusus

# coro manggil seng protected
print(yin._protected)
# iki cukup nggowo coro biasa wes iso di panggil