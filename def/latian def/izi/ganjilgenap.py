#cek ganjel genep
def cek_ganjil_genap(angka):
    if angka % 2 == 0:
        return "genap"
    else:
        return "ganjil"

cek = int(input("Masukkan Angka : "))

hasil = cek_ganjil_genap(cek)
print(f"angka {cek} : {hasil}")
