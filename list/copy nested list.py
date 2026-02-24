data_1 =[1,2]
data_2 =[3,4]

data_gabung =[data_1,data_2,5]
print(f"data gabung : {data_gabung}")

#jajal copy
data_copy = data_gabung.copy()
print(f"Data copy = {data_copy}")

#cek address e
print(f"Addres asli : {hex(id(data_gabung))}")
print(f"Addres copy : {hex(id(data_copy))}")
#nek kene address e iso bedo

#cek address seng list njerone
print(f"Addres asli : {hex(id(data_gabung[0]))}")
print(f"Addres copy : {hex(id(data_copy[0]))}")
#nah iki address podo,dadine mok ngopy njobone tok
"""
Tek ngopy ne nggowo(.copy()) tok,nko iku mok ngopy
njobone tok ngono lo.iku kan list nek njero list,
nah seng di copy iku list jobone tok,orak tekan njero njero.
"""
#jajal tes
data_gabung[1][0] = 5
print(f"data asli :{data_gabung}")
print(f"data copy :{data_copy}")
#nek kene iki mok tak ubah seng data gabung
#tapi hasil ouput e malah ke ubah 2 karone

data_gabung[2] = 10
print(f"data asli :{data_gabung}")
print(f"data copy :{data_copy}")
#iki buktine 

#cara ngopyne
from copy import deepcopy
data_gabung =[data_1,data_2,5]
data_deepcopy =deepcopy(data_gabung)

#tes deepcopy
print("\ndata deep copy")
print(f"data asli :{data_gabung}")
print(f"data deepcopy :{data_deepcopy}")

print(f"Addres asli : {hex(id(data_gabung))}")
print(f"Addres deepcopy : {hex(id(data_deepcopy))}")

#cek address seng list njerone
print(f"Addres asli : {hex(id(data_gabung[0]))}")
print(f"Addres deepcopy : {hex(id(data_deepcopy[0]))}")