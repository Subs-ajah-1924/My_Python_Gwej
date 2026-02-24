#loop list

print("Menggunakan for")

data = [1,2,3,4,5]

for i in data:
    print(f"data : {i}")

print("\nMenggunakan for range")
data = [1,5,3,4,7]

for i in range(len(data)):
    print(f"Data : {i}")

print("\nmenggunakan while")

ongko =[3,5,7,2,8,4]
itungan = 0
panjang = len(ongko)

while itungan < panjang:
    print(f"Data : {ongko[itungan]}")
    itungan += 1

    
print("\nList Komprehension")
angka =[3,5,7,2,8,4]
[print(f"data :{i}") for i in angka]
angka =[3,5,7,2,8,4]
angka_kuadrat =[i**2 for i in angka]
print(angka_kuadrat)


print(f"enumerate")
ongko =[3,5,7,2,8,4]

for i,angka in enumerate(ongko):
    print(f"index :{i} , data :{angka}")


