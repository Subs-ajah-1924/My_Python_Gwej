#lambda function

#function biasa
def kuadrat(angka):
    return angka**2

print(f"kuadrat tanpa lambda : {kuadrat(5)}")

#contoh dengan lambda
#output = lambda argumen: expression

kuadrat = lambda angka:angka**2
print(f"kuadrat lambda : {kuadrat(5)}")

#lambda argumen ganda
jumlah = lambda angka1,angka2:angka1+angka2
print(f"jumlah lambda : {jumlah(5,6)}")


##kegunaan e opo

#sorting list biasa
data_list = ["subahehe","jos","mbuh"]
data_list.sort()
print(f"sorted list : {data_list}")

#sort nggowo panjang
data_list = ["subahehe","jos","mbuh"]
def panjang_list(nama):
    return len(nama)

data_list.sort(key=panjang_list)#tek pengen sort panjang kudu ono key ne,di kei(len)
print(f"sorted list panjang : {data_list}")

#sort panjang lamda
data_list = ["subahehe","jos","mbuh"]
data_list.sort(key=lambda nama:len(nama))
print(f"sorted list panjang lambda : {data_list}")

data_angka = [1,2,3,4,5,6,7,8,9,10,11,12]
#contoh dengan def
def kurang_dari_5(angka):
    return angka < 5
data_angka_anyar = list(filter(kurang_dari_5,data_angka))
print(data_angka_anyar)

#contoh nggowo lambda

data_angka_anyar = list(filter(lambda x:x<5,data_angka))
print(data_angka_anyar)

#gawe genap kabeh
data_genap = list(filter(lambda genap:genap % 2 == 0,data_angka))
print(data_genap)

#data ganjil
data_ganjil = list(filter(lambda ganjil:ganjil % 2 != 0,data_angka))
print(data_ganjil)

#data kelipatan
data_kelipatan = list(filter(lambda kelipatan:kelipatan % 4 == 0,data_angka))
print(data_kelipatan)

#anonymous function
#currying

def pangkat(n):
    return lambda angka:angka**n

pangkat2 = pangkat(2)
print(f"pangkat 2 adalah : {pangkat2(5)}")
pangkat3 = pangkat(3)
print(f"pangkat 3 adalah : {pangkat3(4)}")
#iku gampangane iso di ubah sembarang fungsine
#misal neh

print(f"pangkat bebas : {pangkat(5)(2)}")