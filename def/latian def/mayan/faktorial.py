#faktorial

def faktorial(x):
    if x < 0:
        return "Faktorial tidak Menerima Bilangan Negatif"
    elif x == 0:
        return 1
    else:
        faktorial = 1
        for i in range(1,x+1):
            faktorial *= i
        return faktorial
    
angka = int(input("Masukkan Angka : "))
hasil = faktorial(angka)
print(f"Hasil Faktorian dari {angka} : {hasil}")
