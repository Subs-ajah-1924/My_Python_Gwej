#date dan time (latihan)

import datetime as dt

#iki otomatis dino iki nggowo "today"
dino_iki = dt.date.today()
print(dino_iki)
print(f"hari ini adalah hari : {dino_iki:%A}")# %A kanggo dino 

#iki seng manual gasah nggowo "today"
tanggal = dt.date(2006,8,14)
print(f"hari ini adalah hari : {tanggal:%A}")

print("\n\n")

print(5*"="+" Silahkan Masukkan tanggal,bulan,dan tahun lahir anda "+5*"=")
tanggal =int(input("masukkan tanggal lahir : "))
bulan =int(input("masukkan bulan lahir   : "))
tahun =int(input("masukkan tahun lahir : "))

print("\n")
print(5*"="+"tanggal dan hari lahir"+5*"=")
lahir = dt.date(tahun,bulan,tanggal)
print(f"tanggal lahir anda adalah : {lahir}")
print(f"hari lahir anda adalah     : {lahir:%A}")

#penghitung umur

print("\n")
print(5*"="+"umur anda"+5*"=")
hari_ini = dt.date.today()
print(f"hari ini adalah : {hari_ini}")
umur_hari = hari_ini - lahir
umur_tahun = umur_hari.days // 365 #diwei ".days" ben days nek run e ilang 
print (f"umur anda adalah : {umur_tahun}")


date = dt.datetime(tahun,bulan,tanggal)
print(date)
