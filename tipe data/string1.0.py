#operasi string apik 

#1.Menggabungkan String

nama_1 = "Muhammad"
nama_2 = "Mufthi"
nama_3 = "Dafus"
nama_4 = "Subah"

nama_lengkap = nama_1 + nama_2 + nama_3 + nama_4
print (nama_lengkap)

#1.Menggabungkan String tambah sepasi

nama_1 = "Muhammad"
nama_2 = "Mufthi"
nama_3 = "Dafus"
nama_4 = "Subah"

nama_lengkap = nama_1 + " " + nama_2 + " " + nama_3 + " " + nama_4
print (nama_lengkap)

#2.ngitong panjang string e (len)

panjang = len(nama_lengkap)
print ("panjang dari " + nama_lengkap + " adalah :",panjang)

#3.ngecek ono komponen char utowo string nek njero string e ta orak

#iki seng bener
a = "Subah"
status = a in nama_lengkap
print(a+" di dalam "+nama_lengkap+" adalah :"+str(status))

#iki seng salah
a = "subah" # "s" e cilek salah dadine
status = a in nama_lengkap
print(a+" di dalam "+nama_lengkap+" adalah :"+str(status))

#iki kanggo luru seng gaono (not in)

a = "Subah"
status = a not in nama_lengkap
print(a+" di dalam "+nama_lengkap+" adalah :"+str(status))

# 4.pengulangan string

print(3*"awok")
print("awok"*3)

# 5. Indexing (jupok jupok "[]")

print("index ke-0 :"+nama_lengkap[0])#iki mulaine ko "m" berarti
print("index ke-5 :"+nama_lengkap[5])
print("index ke-(-1) :"+nama_lengkap[-1])#iki jupok seng mburipol tek mines (-)
print("index ke-(-3) :"+nama_lengkap[-3])
print("index ke-[0-7] :"+nama_lengkap[0:8])#iki kudune seng ongko mburi tambahi 1 ben akurat
print("index ke-[4-8] :"+nama_lengkap[4:9])#[4-8] trs kudune [4-9] ben apik
print("index ke (0,3,6,9,12,15,18,21,24,27) :"+nama_lengkap [0:27:3])

# 6. besar/kecil

#paling besar
print("paling besar :"+max(nama_lengkap))
#paling kecil
print("paling kecil :"+min(nama_lengkap))
#coro ngecek e
ascii_code = ord (" ") #iki spasi
print("ASCII code untuk spasi adalah :"+str(ascii_code))
data = 99 
print("char untuk angka 99 adalah :"+chr(data))
