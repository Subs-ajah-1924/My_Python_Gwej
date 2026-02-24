haha = {
    "haha":"jajaja",
    "jaja":"subahehe",
    "bruh":"heheheha"
}

hehe = haha.copy()

print(f"haha = {haha}")
print(f"hehe = {hehe}\n")

haha["jaja"]="bruuuuuuhh"
print(f"haha = {haha}")
print(f"hehe = {hehe}\n")

#pop dictinary
databruh = haha.pop("bruh")
print(f"haha = {haha}")
print(f"hehe = {hehe}")
print(f"data bruh = {databruh}")#iki jupok data

#popitem dictionary
data_terakhir=haha.popitem()#iki kanggo jupok data paleng terakher(popitem)
print(f"data terakhir = {data_terakhir}")
print(f"haha = {haha}")
