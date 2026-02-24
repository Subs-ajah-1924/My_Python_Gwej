import datetime
import os
import string
import random

#data template

data_template = {
    'nama':'nama',
    'nim':'000000000000',
    'sks':0,
    'lahir':datetime.datetime(1111,1,1)
}
data_mahasiswa = {}

while True:
    os.system("cls")
    mahasiswa = dict.fromkeys(data_template.keys())

    mahasiswa['nama'] = input("Masukkan Nama :")
    mahasiswa['nim'] = input("Masukkan NIM :")
    mahasiswa['sks'] = int(input("Masukkan SKS :"))
    TAHUN = int(input("Masukkan Tahun Lahir(YYYY):"))
    BULAN = int(input("Masukkan Bulam Lahir(1-12):"))
    TANGGAL = int(input("Masukkan Tanggal Lahir(1-31):"))
    mahasiswa['lahir'] =datetime.datetime(TAHUN,BULAN,TANGGAL)

    KEY = ''.join((random.choice(string.ascii_uppercase)for i in range(6)))
    
    data_mahasiswa.update({KEY:mahasiswa})

    print(f"{'KEY':<6} {'NAMA':<20} {'NIM':<13} {'SKS':<3} {'LAHIR':<9}")
    print("-"*50)


    for mahasiswa in data_mahasiswa:
        KEY = mahasiswa
        
        NAMA = data_mahasiswa[KEY]['nama']
        NIM = data_mahasiswa[KEY]['nim']
        SKS = data_mahasiswa[KEY]['sks']
        LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")
        print(f"{KEY:<6} {NAMA:<20} {NIM:<13} {SKS:<3} {LAHIR:<9}")
  
    done = input("apakh sudah bar(y/n)?")
    if done == "n":
        break
    


