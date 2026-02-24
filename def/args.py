#*args pada fungsi

#fungsi biasa
#contoh list e
def fungsi(apik):
    data = apik.copy()
    nama = data[0]
    umur = data[1]
    berat = data[2]
    print(f"{nama},\numur :{umur},\nberat :{berat}")

fungsi(["subahehe",180,65])#iki aren nggo dobel kurong ngene
#iku list e harus nesuaino banget karo fungsi nek njerone
#carane ben penak nggowo args(*argument)
#contoh args(*argument)

def list_args(*conto_list):
    nama = conto_list[0]
    umur = conto_list[1]
    berat = conto_list[2]
    print(f"{nama},\numur :{umur},\nberat :{berat}")
    
list_args("subahehe",180,65)

#contoh liane

def tambah(*angka):
    output = 0

    for ongko in angka:
        output += ongko

    return output
hasil = tambah(1,2,3,4,5,6,7,8,9)#data seng di masokno iso fleksibel,rak perlu manut argument e
print(f"hasil : {hasil}")
hasil = tambah(23,54,67)
print(f"hasil : {hasil}")

