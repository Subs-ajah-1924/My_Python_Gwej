data_0 =[1,2,3]
data_1 =[4,5,6]

data_list_biasa = [1,2,3,4,5,6]

print(f"data list : {data_list_biasa}")

#gabong list e
list_2D =[data_0,data_1]
print(f"list gabungan : {list_2D}")
#iki iso di imbohi opo wae
list_2D_tambah =[data_0,data_1,2,3,"ya ya saya stuju"]
print(f"list gabungan : {list_2D_tambah}")

#Jupok data nested list

data_0 =[1,2,3]
data_1 =[4,5,6]
#index e    0      1
list_2D =[data_0,data_1]
print(f"data : {list_2D}")

#jupok e
data = list_2D[1][0]
print(f"Data jupok an : {data}")


#contoh asik e

peserta_0 =["subah",18,"Lanang"]
peserta_1 =["hehe",23,"Lanang"]
peserta_2 =["alok",45,"Wedok"]

jumlah_peserta =[peserta_0,peserta_1,peserta_2]

print(f"Peserta : {jumlah_peserta}")

for peserta in jumlah_peserta:
    print(f"Nama : {peserta[0]}")
    print(f"Umur : {peserta[1]}")
    print(f"Kelamin : {peserta[2]}\n")

