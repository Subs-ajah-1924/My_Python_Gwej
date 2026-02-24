#**kwargs pada fungsi
#gampangane ngene :
#tek *args iku dadi list
#tek **kwargs dadi dictionary
#fungsi biasa
def fungsi(nama,umur,berat):
    print(f"nama:{nama} ,usia:{umur} ,berat:{berat}")

fungsi("subahehe",170,76)

#contoh **kwargs
def fungsi(**data):
    '''fungssi kwargs'''
    nama =data["nama"]
    usia =data["usia"]
    berat =data["berat"]
    print(f"nama:{nama} ,usia:{usia} ,berat:{berat}")
    
fungsi(nama="subahehe",usia=23,berat=233)


#contoh keren e
def math(*angka,**option):
    output = 0
    if option["option"] == "tambah":
        for numer in angka:
            output += numer
    elif option["option"] == "kali":
        output=1
        for numer in angka:
            output *= numer
    else:
        print("tidak ada program")

    return output

hasil = math(2,3,45,5,6,3,option ="tambah")
print(f"hasil tambah : {hasil}")
hasil = math(2,3,option ="kali")
print(f"hasil kali : {hasil}")
