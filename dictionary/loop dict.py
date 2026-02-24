#loop dictionary


haha = {
    "haha":"jajaja",
    "jaja":"subahehe",
    "bruh":"heheheha"
}

for wkwkw in haha:
    print(wkwkw) #iki metune mok key ne tok rak iso kabeh
print(" ")

#nggolek keys
keys = haha.keys() #keys iki kanggo nggolek key ne tok
print(keys) 
print(" ")
for key in haha.keys():
    print(haha.get(key)) #coro ribet nggolek value
print(" ")

#nggolek value
value = haha.values()
print(value)
print(" ")
for value in haha.values():
    print(value)
print(" ")

#nggolek item
item = haha.items()
print(item)

for key,value in haha.items():
    print(f"key = {key} ,value  = {value}")



