#--LIST--

#list adalah kumpulan data
#1)data data nomor
list_nomor = [1,2,3] #nggowone kurung kotak
print(list_nomor)
#2)data data string
list_string = ["akulah","atomik"] #nggowone kurung kotak
print(list_string)
#3)data data boolean
list_bool = [True,False,False,True] #nggowone kurung kotak
print(list_bool)
#4)data data campuran
list_campur = [1,"aku",True] #nggowone kurung kotak
print(list_campur)

#5)list dengan range
data_range = range(1,10)
print(data_range)
list_range = list(data_range)
print(list_range)

#6)list dalam for
list_pake_for = [i**2 for i in range(1,10)]
print(list_pake_for)

#7)list dengan for dan if
list_pake_for_if = [i for i in range(1,10) if i%2 ==0] #[hasil for item in iterable if kondisi]
print(list_pake_for_if)

list_pake_for_if = [i for i in range(1,10) if i%2 !=0]
print(list_pake_for_if)
