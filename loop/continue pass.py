#pass dan continue

#pass = berfungsi sebagai dummy,tidak akan dieksekusi
#mbuh kanggone opo jeh gareti asli 

# halo iki aku masa depan
# pass iku kanggo nyekip ongko seng di pileh gampangane,tapi fungsi ne iku luweh kanggo penambal ben orak ketok erroe

angka = 0 

while angka < 5:
    angka +=1

    if angka == 3:
        pass #gampangane kanggo nembel sementara beniso ngecek run run na ne sek 
             #ngono lah penak e mugo mugo sok tek moco iki mudeng neh
    print(angka)

#=========================================================================================

#loop = kyok muter muter trs nko iso di barno
#continue = gampangane kyok iso motong loop e dadine langsong menduwor neh

angka = 0 

while angka <5:
    angka+= 1
    print(f"angka sebelumnya {angka}")

    if angka == 3 :
        print("jos")
        continue    #pomo gak nggowo iki nko ke print seng no 3 iku ngene
                    #angka sebelumnya (\n) jos (\n) gege gemink 

    print("gege gemink")

#dadi continue iku kanggo mekso ben lanjot ngo menduwor loop e orak lanjot mengisor sek

#=========================================================================================

#break = lawane continue,break iki pomo wes tekan langsong mandekno loop e ,ogk di lamjotno
#neh koyok continue

angka = 0 

while angka < 5:
    angka += 1
    print (f"yatta {angka}")

    if angka == 3:
        print("watdesigma")
        break #nah iki pomo loop ke 3 nko langsong mandek

    print("maynkraf lagi kia=ta coyy")
print("bar")

#contoh 2

data_int = int(input("poll piro pengen loop mu ? :"))

angka = 0 

while True:
    angka += 1
    print (f"yatta {angka}")

    if angka == data_int:
        print("watdesigma")
        break #nah iki pomo loop ke 3 nko langsong mandek

    print("maynkraf lagi kia=ta coyy")
print("bar")