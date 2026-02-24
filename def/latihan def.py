#program luas persegi panjang

import os

def header():
    '''header'''
    os.system("cls")
    print(f"{"Program Menghitung Luas":^40}")
    print(f"{"Dan Keliling Persegi Panjang":^40}")
    print(f"{"-"*40:^40}")
    print("Pilih Program:")
    print("0.keliling")
    print("1.luas")
    print("2.Keliling dan Luas")

def input_user():
    '''input user'''
    panjang = int(input("Masukkan panjang : "))
    lebar = int(input("Masukkan lebar : ")) 
    return panjang,lebar

def luas(panjang,lebar):
    return panjang*lebar

def keliling(panjang,lebar):
    return 2 * (panjang + lebar)

def display(message,value):
    print(f"hasil perhitungan {message} = {value}")

def display_0():
    ''' keliling '''
    PANJANG,LEBAR = input_user()
    KELILING = keliling(PANJANG,LEBAR)
    display("Keliling = ",KELILING)

def dispay_1():
    '''luas'''
    PANJANG,LEBAR = input_user()
    LUAS = luas(PANJANG,LEBAR)
    display("Luas = ",LUAS)

def display_2():
    PANJANG,LEBAR = input_user()
    LUAS = luas(PANJANG,LEBAR)
    KELILING = keliling(PANJANG,LEBAR)

    display("Luas = ",LUAS)
    display("Keliling = ",KELILING)


while True:
    header()
    opsi =int(input("Pilih program :"))
    if opsi == 0:
        display_0()
    elif opsi == 1:
        dispay_1()
    elif opsi == 2:
        display_2()
    else:
        print("jos")

    lanjut=input("Apakah Lanjut(y/n)?")
    if lanjut == "n":
        break
print("Akhir Dari Program")
