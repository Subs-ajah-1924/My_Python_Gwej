""" Fungsi dengan kembalian"""

#template
#def fungsi(argument):
#   operasine
#   return output

#fungsi kuadrat

def kuadrat(angka):
    '''fungsi kuadrat'''
    hasil = angka**2
    return hasil


print(kuadrat(2))#iki pomo gak nggo return gak iso langsong di print ngene,kudune diwei variabel sek ngarepe
pangkat_2 = kuadrat(7)
print(pangkat_2)
print(pangkat_2 + 1)


#fungsi tambah(dengan dua argument)

def tambah(angka_1,angka_2):
    '''fungsi tambah'''
    return angka_1 +angka_2#iki iso langsong nek return e teek operasine sitik

print(tambah(77,33))

#fungsi multi argument

def aritmatika(angka_3,angka_4):
    tambah = angka_3 + angka_4
    kurang = angka_3 + angka_4
    kali = angka_3 * angka_4
    bagi = angka_3 / angka_4
    return tambah,kurang,kali,bagi

a,b,c,d = aritmatika(8,98)#carane ngene ben iso apik
print(f"hasil : {a}")
print(f"hasil : {b}")
print(f"hasil : {c}")
print(f"hasil : {d}")
