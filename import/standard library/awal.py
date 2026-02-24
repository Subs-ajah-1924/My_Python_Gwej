import datetime

wektu = datetime.datetime.now()
print(f"datetime now : {wektu}")
print(f"tahun : {wektu.year}")
print(f"hari : {wektu.strftime('%A')}")

from collections import Counter

data = ["a","s","a","r","b","b","b"]
data_count = Counter(data)
print(data_count) #hasile dictionary
print(f"data a : {data_count['a']}")
print(f"data b : {data_count['b']}")


import io #membaca teks

file = io.open("hehehe.txt","r")
print(file.read())
