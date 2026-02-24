#sarjana importir

# iki 
#  sonnano yuumei piikara piikara

# print
print("halo dunia")

# variable singkat
nama = "subahehe"
umur = 30

print(f"halo namaku {nama},gwe berumur {umur}")

# tipe data 
string = "subahehe"
integer = 30
floatDesimal = 30.1
Boolean = True
Boolean = False 


# aritmatika
number_1 = 10
number_2 = 2

print(number_1 + number_2)
print(number_1 - number_2)
print(number_1 * number_2)
print(number_1 / number_2)
print(number_1 ** number_2) #pangkat
print(number_1 // number_2) #division()hasil pembagian)
print(number_1 % number_2) #modulus(sisa pembagian)

# assignment(versi singkat pomo ape jumlahno variable seng podo)
number_1 += number_2
number_1 -= number_2
number_1 *= number_2
number_1 /= number_2
number_1 **= number_2
number_1 //= number_2
number_1 %= number_2

# operator pembanding(hasile mesti boolean)
hasil=number_1 > number_2
print(f"hasil dari > adalah : {hasil}")
hasil=number_1 < number_2
print(f"hasil dari < adalah : {hasil}")
hasil=number_1 >= number_2 #tek ono samadengan e iku tek ongokne podo iku hasile true
print(f"hasil dari >= adalah : {hasil}")
hasil=number_1 <= number_2
print(f"hasil dari <= adalah : {hasil}")
hasil=number_1 == number_2
print(f"hasil dari = adalah : {hasil}")
hasil=number_1 != number_2
print(f"hasil dari != adalah : {hasil}")

# is iku fungsine mirip kyok "==" yaiku kedua hal podo percis tarak,tapi iki tergantung cara pythone nyimpen datane.iki orak kanggo ongko tok,tapi iso mbandengno objek podo

hasil = number_2 is number_1 #tidak disarankan 
print(f"hasil perbandingan angka : {hasil}")

arr = [1,2,3] #iki nek memori mesti bedo karo arr ngisore walaupun isine podo
arr_1 = [1,2,3]

hasil = arr is arr_1
print(f"hasil arr = {hasil}")

hasil = arr is not arr_1
print(f"hasil arr = {hasil}")

# logika 
# === and === (harus podo loro karone,pomo orak hasile False)
a = True
b = False
c = a and b
print(c)
# === or == (misal salah siji True hasile True)
a = True
b = False
c = a or b
print(c)
# === not == (walikane gampangane)
a = True
b = not a
print("== not ==")
print(a)
print(b)
# === xor == (tek ono seng kembar 2 = False)
a = True
b = True
c = a ^ b
print(c)


# if statement
nilai = 5
if nilai > 5:
    print("angka lebih dari 5")
elif nilai == 5:
    print("angka bernilai 5")
else:
    print("angka kurang dari 5")


# loop
for i in range(nilai):
    print(f"ini loop ke -{i + 1}")

while nilai < 10:
    print("ini loop asik")
    nilai += 1

# pass dan continue

# pass
namba = 0
while namba < 10:
    namba += 1

    if namba == 6:
        pass
    else:
        print(f"ini loop ke {namba}")

# continue
angka = 10
target = 5
for i in range(angka):
    print("mencari target:")
    if i == target:
        print(f"target di temukan yaitu angka {target}")
        continue

    print("target belum di temukan")


# === tipe data lanjut ===


# === String ===
# menggabungkan sting
nama_1 = "Muhammad"
nama_2 = "Mufthi"
nama_3 = "Dafus"
nama_4 = "Subah"

# menggunakan +
nama_lengkap = nama_1 +" " + nama_2 + " " + nama_3 + " " + nama_4
print(nama_lengkap)
print("nama gwe adalah "+ nama_4 + "ehe")

# tanda slash
print("C:\\Subahehe\\Document")
# tab
print("nama\t: M.Mufthi Dafussubah")
print("NIM\t: 241240001523")
# backspace(ngehapus mburine seng slash e iku)
print("asu \bkayang")
# new line
print("\nadalah gwe")
print("baris pertama.\rbaris") #kyok kursormu di balekno ngo awal neh.dadi nko di tules baris pertama sek,nah bariku di timpa huruf setelah \r iku.ngono lah ya

# f dan r string
print(f"halo ini gwe {nama_4}")
print(r"C:\new Folder") #gampangane matikno escape sequence


# ngecek nama ono neng jero tarak
status = nama_4 in nama_lengkap
print(f"{nama_4} di dalam {nama_lengkap} adalah {status}")

# kali string
print(3*"awok")
print("awok"*3)

# indexing 
print(f"index ke 3 dari {nama_4} adalah {nama_4[3]}")
print(f"index ke-(0-3) dari {nama_lengkap} adalah {nama_lengkap[0:3]}")

#paling besar
print("paling besar :"+max(nama_lengkap))
#paling kecil
print("paling kecil :"+min(nama_lengkap))
#coro ngecek e
ascii_code = ord (" ") #iki spasi
print("ASCII code untuk spasi adalah :"+str(ascii_code))
data = 99 
print("char untuk angka 99 adalah :"+chr(data))

# casting tipe data
data = 10
data_float = float(data)
data_string = str(data)
data_bool = bool(data)
data_int = int(data)

# widht dan alignment
nama = "Subahehe"
umur = 99
tinggi = 108.213
sepatu = 43
data_string = f"""
nama\t: {nama:<20}   #rata kiri
umur\t: {umur:^20}   #iki ngo tengah
tinggi\t: {tinggi:>20.2f}   # iki ngo kanan
sepatu\t: {sepatu:^20} """
print("\n"+5*"="+"My data gwe"+5*"=")
print(data_string)


# === LIST ==
data_list = [1,"subahehe",True,4.1]

# data list menggunakan range
data_range = range(1,10)
data_list = list(data_range)
print(data_list)

# for di dalam list
for_list = [i**2 for i in range(1,10)] #iki hasile list trs dipangkat jerone
print(for_list)

# for dan if di dalam list
for_dan_if_list = [i for i in range(1,10) if i%2 == 0] #iki jikok ongko senga genep tok
print(for_dan_if_list)

for_dan_if_list = [i for i in range(1,10) if i%2 != 0] #iki jikok ongko senga ganjil tok
print(for_dan_if_list)


# === data tuple dan set ===
# data tuple : intine datane rak iso ddi kapak kapakno(immutable)
data_tuples = (1,2,3,4,5,6)
print(data_tuples)
print(data_tuples[1])

# data set : data nek jero rak iso dobel dan tidak memiliki index 
data_sets = {10,2,3,3,6,4,10,4}
print(data_sets) #jika di print hasilnya akan terurut
#  operasinya 
a = {1,2,3}
b = {3,4,5}

print(a & b)  # irisan
print(a | b)  # gabungan
print(a - b)  # selisih

# === Manipulaisi List ===
data_angka = [1,2,3,1,3,2,4,5,4,7,8,3,7,5,2,1,1,9,7,5,4]

# mencari data int spesifik 
jumlah_data_1 = data_angka.count(1)
jumlah_data_4 = data_angka.count(4)

print(f"jumlah angka 1 : {jumlah_data_1}")
print(f"jumlah angka 4 : {jumlah_data_4}")

# indexing
print(data_angka[1]) #iki mulai tko ngarep
print(data_angka[-2]) #iki mulai tko mburi

data_nama = ['subahehe','gwe','jos']
print(data_nama.index("subahehe")) #jika menggunaaknn data langsung

# sorting list
data_angka.sort()
print(f"data terurut = {data_angka}")

# reverse list 
data_angka.reverse()
print(f"data di balik = {data_angka}")