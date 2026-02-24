#operator dalam bentuk metods

#merubah case dari string

#merubah semua ke upper case

print("----UPPER----")
tawa = "gelak jawa"
print("normal : "+tawa)
tawaluxu = tawa.upper()
print("upper : "+tawaluxu)

#merubah semua ke lower case

print("----LOWER----")
tawa = "GELAK JAWA"
print("normal : "+tawa)
tawaluxu = tawa.lower()
print("upper : "+tawaluxu)

#pengecekan nggowo isN 

print("----LOWER karo UPPER----")
emm = "wat de sigma"
print("variabel : "+emm)
emm_lower = emm.islower()#iki hasil e bool dadine di ubah ngo string sek (str)
print("apakah lower : "+str(emm_lower))
emm_upper = emm.isupper()#iki podo nduwor
print("apakah upper : "+str(emm_upper))

#contoh lio

#istitle()
judul = "Make Heroine Ga Oosugiru!"
cek_judul =judul.istitle()#iki dadine bool podo
print(judul +" apakah istitle : "+ str(cek_judul))
#iku tek ono seng huruf ecilek dadine false
#tek ono kyok larahan misal ',",* karo lia liane

judul = "Make heroine Ga Oosugiru!"
cek_judul =judul.istitle()#iki dadine bool podo
print(judul +" apakah istitle : "+ str(cek_judul))

#isalpha
hurof = "bahakurakmangkatsek"
cek_alpha = hurof.isalpha()#dadi bool
print(hurof + " apakah isalpha : " + str(cek_alpha))
#tek ono spasine dadi false
#tek ono larahane dadi false podo

hurof = "bah aku rak mangkat sek"
cek_alpha = hurof.isalpha()
print(hurof + " apakah isalpha : " + str(cek_alpha))

#isalnum

apik = "knjdbdg888"
cek_alnum = apik.isalnum()
print(apik + "apakah alnum : " + str(cek_alnum))

apik = "knjdbdg 888"
cek_alnum = apik.isalnum()
print(apik + "apakah alnum : " + str(cek_alnum))

#starswith dan endswith 

print("---AWAL karo AKHIR---")
awal = "halo orang sigma".startswith("halo")
print("start : " + str(awal))
awal = "halo orang sigma".startswith("orang")
print("start : " + str(awal))
akhir ="halo orang sigma".endswith("sigma")
print("end : " + str(akhir))
akhir ="halo orang sigma".endswith("halo")
print("end : " + str(akhir))

#gabung pisah (join/split)
print("---GABUNG/PISAH---")
pisah = ['emm','wat','the','sigma']
gabungan = ' '.join(pisah)#seng nek iki ('') iku gabungnone nggowo seng nek njero kono
print("gabungan : "+gabungan)
gabungan = '-'.join(pisah)#seng nek iki ('') iku gabungnone nggowo seng nek njero kono
print("gabungan : "+gabungan)
print ("\n")
gabungan = "emm wat the sigma"
print("pisah :",gabungan.split(' '))
gabungan = "emm  wat  the  sigma"
print("pisah :",gabungan.split('  '))

##alokasi karater rjust() , ljust() , center 

b =("\nalokasi karakter .rjust() , .ljust () , .center ")
bg = b.upper()
print(bg)
#kanan(.rjust())
kanan ="kanan".rjust(10)
print("kanan : " + kanan)
#kiri(ljust())
kiri ="kiri".ljust(10)
print("kiri : " + kiri)
#tengah (center)
tengah ="tengah".center(20)
print("'" + tengah + "'")
tengah ="tengah".center(20,"=")
print("'" + tengah + "'")

#walikane(strip())

a = "STRIP".center(25,"-")
print(a)
kanan ="kanan".strip()
print("kanan : " + kanan)