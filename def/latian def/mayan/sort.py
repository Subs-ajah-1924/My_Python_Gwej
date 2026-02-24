#sorting list
def sort(data_list):
    data_baru = data_list.copy()
    data_baru.sort()
    return data_baru

data_list = [5,46,7,3,2]
data_sort =sort(data_list)
print(data_sort)
