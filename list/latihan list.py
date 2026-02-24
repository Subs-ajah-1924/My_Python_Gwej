#program buku
data_buku =[]

while True:
    nama = input("Nama Penulis\t:")
    buku = input("Judul Buku\t:")
    
    penulis_buku =[nama,buku]
    data_buku.append(penulis_buku)

    for index,buku in enumerate(data_buku):
        print(f"{index + 1}|{buku[0]}\t|{buku[1]}")

    lanjut = input("Apakah ingin lanjut(y/n)?")
    if lanjut == "n":
        break
