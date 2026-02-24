#format string

#contoh generic
apik = "FORMAT STRING".center(30,"=")
print(apik+"\n")

apik = " FORMAT F ".center(20,"=")
print(apik)
#string
nama = "HEHEHEHA"
print(f"siapa namamu tuan ? watashino nama e wa {nama} ,jiahahahahaha")
#(f) iku kanggone ben penak
#conto lio

#boolean
boolean = False 
print(f"boolean adalah: {boolean}")

#ongko
ongko = 2004 
print(f"ongko adalah: {ongko}")

#bilangan bulat (int)
ongko = 2004 
print(f"ongko adalah: {ongko:d}")#nggowone (d) mbuh ben opo,iki tek ono komane dadine false

#bilangan ribuan ke atas 
ongko = 2004 
print(f"ribuan adalah: {ongko:,}")#nggowone (,) ben otomatis ke dokok
ongko = 20040023 
print(f"jutaan adalah: {ongko:,}")#nggowone (,) ben otomatis ke dokok

#bilangan desimal (float)
ongko = 2004.365456
print(f"ongko adalah: {ongko:.2f}")#nggowone (.Nf) N e iku baris e ape mbok jupok piro

#menampilkan leading zero (mbuh)
angka = 5243.846
format_str = f"leading zero :  {angka:010.2f}"#kyok e ben ono nol e , mbuh lah
print(format_str)

#menampilkan tanda + atau - 
mines = -69
ples = 54.67652385
format_mines = f"minus: {mines:+d}"#iki (d) iku sesuai karo bilangane (int)
formmat_ples = f"plus : {ples:+.5f}"#iki nggowo (.Nf) samadengan float
print(format_mines)
print(formmat_ples)

#memformat persen
persen = 0.065
format_persen = f"persen : {persen:.1%}"
print(format_persen)

#tambahan
#nek kurung kurawal iku iso itung itung an

a = 25
b = 4 
hasil = f"hasilnya : {a*b}"
print(hasil)

#format angka lain binary() , hex() , octal()
angka = 445 
format_binary = f"binary : {bin(angka)}"
format_octal = f"octal : {oct(angka)}"
format_hex = f"hex : {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hex)