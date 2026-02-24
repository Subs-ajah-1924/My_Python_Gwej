'''Fungsi dengan argumen'''

#template
#def nama_fungsi(argument):
#   badan fungsi

def hello_world(nama):
    '''Fungsi hello world menerima input dengan variable nama'''
    print(f"Selamat datang {nama}")

hello_world("subahehe")

#program tambah tambah

def tambah(angka_1,angka_2):
    '''Program tambah'''
    hasil = angka_1 + angka_2
    print(f"{angka_1} + {angka_2} = {hasil}")

tambah(4,5)
tambah(3,5)
tambah(6,7)

#masukno list

def halo(orang_orang):
    '''fungsi halo''' 
    orang = orang_orang.copy()#geneo iki ngopy orang_orang,orak list anggota nek ngisor?
    #iku anggota nek ngisor wes di jupok list e,di jupok dokok orang_orang nek nduwur

    for wong in orang:
        print(f"halo {wong}")
    return orang

anggota = ["subahehe","haha","hehe","alok"]
neh = ["mbuh","jos","ya ya sya stuju"]

halo(anggota)
halo(neh)
print(anggota[1])#ini buktinya
