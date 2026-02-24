#pakcage : kumpulan module module (kyok folder lah gampangane)
#cara import e

import sains.matematika #iki biasa
from sains import fisika #iki seng mayan
from sains.matematika import pangkat as kuadrat #iki seng ribet tapi apik

hasil_tambah = sains.matematika.tambah(6,4,3,7,8)
print(f"hasil tambah : {hasil_tambah}")

gaya = fisika.gaya(25,9.8)
print(f"gaya : {gaya}")

pangkat2 = kuadrat(2)
print(f"pangkat 2 adalah : {pangkat2(6)}")