import datetime

mahasiswa1 = {
    'nama':'subahehe',
    'nim':'241240001523',
    'sks':'140',
    'beasiswa':True,
    'lahir':datetime.datetime(2006,8,14)
}
mahasiswa2 = {
    'nama':'alok gaming',
    'nim':'241240001524',
    'sks':'135',
    'beasiswa':False,
    'lahir':datetime.datetime(2001,11,13)
}
mahasiswa3 = {
    'nama':'alu lejen',
    'nim':'241240001525',
    'sks':'130',
    'beasiswa':False,
    'lahir':datetime.datetime(2004,6,11)
}

data_mahasiwa = {
    'MAHA01':mahasiswa1,
    'MAHA02':mahasiswa2,
    'MAHA03':mahasiswa3
}

print(f"{'KEY':<6} {'NAMA':<15} {'NIM':<13} {'SKS':<3} {'BEASISWA':<9} {'LAHIR':<9}")
print("-"*60)

for mahasiswa in data_mahasiwa:
    KEY = mahasiswa

    NAMA =data_mahasiwa[KEY]['nama']
    NIM = data_mahasiwa[KEY]['nim']
    SKS = data_mahasiwa[KEY]['sks']
    BEASISWA = data_mahasiwa[KEY]['beasiswa']
    LAHIR = data_mahasiwa[KEY]['lahir'].strftime("%x")
    print(f"{KEY:<6} {NAMA:<15} {NIM:<13} {SKS:<3} {BEASISWA:^9} {LAHIR:<9}")

