"""Default argument"""

#def fungsi(argument):
#def fungsi(argument = nilai defaultnya)

#contoh 1
def halo(nama = "bang"):
    '''fungsi dengan default argument'''
    print(f"halo {nama}")

halo("subahehe")
halo()#iki pomo gak di isi nko metune default argumene

#contoh 2
def sapa(nama,pesan = "jangan main fesnuk gila"):
    '''fungsi dengan argumen biasa dan argumen default'''
    print(f"halo {nama}, {pesan}")

sapa("bos","piye kabare?")
