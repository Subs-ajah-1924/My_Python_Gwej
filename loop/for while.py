#perulangan (for/while)

#for kondisi:
#   aksi          rumus simple e

#ini dengan list
angka2 = [0,1,2,3,4]
print(angka2)
for i in angka2: #gampangane i ne dadi ongko sesuai karo nek jero list e
    print (f"i sekarangan --> {i}")
print("\n")
angka2 = [4,6,1,9,3]
for i in angka2:
    print (f"i sekarangan --> {i}")
print("\n")

#menggunakan range 
angka_range = range(8)

for i in angka_range:
    print(f"i sekarang -->{i}")

print("\n")
angka_range = range(8)

for i in angka_range:
    print(f"halo rek")#iso nggowo sembarang kaler
print("\n")

#menggunakan string (str)

data_string = "the ship got wreck with"

for huruf in data_string :
    print(huruf)


hehe = 15
while hehe > 10:
    hehe -= 1 #pomo gak di wei iki,nko iso dadi kyok heker
    print("subahehe jos")

