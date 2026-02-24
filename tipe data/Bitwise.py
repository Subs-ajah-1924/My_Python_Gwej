#contoh binary iki 
#misal = int 2        :00000010 = 2 pangkat 1 
#iki podo karo ngene  :76543210
#dadi pomo int 2 dadine ngene
#2 pangkat 1 = 2, gampangane ngger ono ongko 1 iku dadekno pangkat kanggo ongko 2
#misal neh : 000001001 = 2 pangkat 4 + 2 pangkat 0 = 17
#bitwise = operasi masing-masing bit,gampangane kyok nggawe sistem operasi nganggo 2 binary

#gas contone 
a = 7
b = 4
c = a | b
print("\n===========(OR)==========(|)")
print("nilai : ",a, ' ,binary : ',format (a,'08b'))
print("nilai : ",b, ' ,binary : ',format (b,'08b'))
print("--------------------------------------------- (|)")
print("nilai : ",c, ' ,binary : ',format (c,'08b'))

print("\n===========(AND)==========(&)")
c = a & b
print("nilai : ",a, ' ,binary : ',format (a,'08b'))
print("nilai : ",b, ' ,binary : ',format (b,'08b'))
print("--------------------------------------------- (&)")
print("nilai : ",c, ' ,binary : ',format (c,'08b'))

print("\n===========(XOR)==========(^)")
c = a ^ b
print("nilai : ",a, ' ,binary : ',format (a,'08b'))
print("nilai : ",b, ' ,binary : ',format (b,'08b'))
print("--------------------------------------------- (^)")
print("nilai : ",c, ' ,binary : ',format (c,'08b'))

print("\n===========(NOT)==========(~)")
c =  ~ a
print("nilai : ",a, ' ,binary : ',format (a,'08b'))
print("--------------------------------------------- (~)")
print("nilai : ",c, ' ,binary : ',format (c & 0xFF,'08b'))
#geneo iku dadi -8?mbuh podo gamudeng tapi jare lik e pomo not nko mesti hasil e ngluweh i 1 
#teko ongko seng di (not) no
#ono coro lio nggowo (& 0xFF)
print("nilai : ",c, ' ,binary : ',format (c & 0xFF,'08b'))

#shift (geser)
#sifth right
print("\n===========(GESER)==========(>> / <<)")
c = a >> 1
print("nilai : ",a, ' ,binary : ',format (a,'08b'))
print("--------------------------------------------- (>>)")
print("nilai : ",c, ' ,binary : ',format (c,'08b'))
print ("\n")
c = a << 1
print("nilai : ",a, ' ,binary : ',format (a,'08b'))
print("--------------------------------------------- (<<)")
print("nilai : ",c, ' ,binary : ',format (c,'08b'))
#intine geser lah iso dingeti ongko 1 karo 0 le 
#tek bingong iki ('08b'),artine seng 08 iku kyok itungane misal : 00000010 = 8 baris ongko
#tek iki ('04b'),artine seng 04 iku kyok itungane misal : 0010 = 4 baris ongko

# ngetik opo tah bah subah





