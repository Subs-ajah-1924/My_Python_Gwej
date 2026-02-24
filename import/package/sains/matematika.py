def tambah(*angka):
    hasil =  0
    for ongko in angka:
        hasil += ongko
    return hasil

def kali(*angka):
    hasil = 1
    for ongko in angka:
        hasil *= ongko
    return hasil

def pangkat(n):
    return lambda angka:angka**n

def bagi(angka1,angka2):
    return angka1 / angka2