#__init__ : kanggo di eksekusi disek pas ngimport package e (sesimpel iku)
import sains # package sains iki gaono opopo ne sak jane

from sains.emteka import scientific
#cara ndokok e y nggowo __init__
#misal nggawe folder anyar njerone di wei __init__ ben ke detek init seng nek njobo
hasil_tambah = sains.emteka.tambah(2,3,4,5,6,6)
print(f"Hasil Tambah : {hasil_tambah}")

gaya = sains.fisika.gaya(10,9.8)
print(f"gaya : {gaya}")

hasil_kali = sains.emteka.kali(1,2,3,4,5)#iki matematika ne ws langsong ke import nek init e
print(f"Hasil kali : {hasil_kali}")

hasil_pangkat3 = scientific.pangkat(3)#iki matematika ne ws langsong ke import nek init e
print(f"Hasil pangkat : {hasil_pangkat3(4)}")
