#opersi dict


data_dict = {
    'sbh':'subahehe',
    'wfu':'waifu',
    'hh':'haha',
    'heh':'hehe'
}

# menghitung panjang dict
 
LENDICT = len(data_dict)
print(F'panjang data dict adalah : {LENDICT}')

# Key :ngecek key seng nek njero datane ono porak
KEY = 'hh'

KEYDICT = KEY in data_dict
print(f'apakah key {KEY} di data dict : {KEYDICT}')

# get (jupok)

print(data_dict['sbh'])
print(data_dict.get('sbh'))
print(data_dict.get('ha')) 
print(data_dict.get('ha','key tidak ada di data'))

##nambahi / ngapdet

#coro biasa
data_dict['sbh'] = 'subahehehejos'
print(data_dict)

data_dict['jaja'] = 'ingfokan'
print(data_dict)

#coro jos
data_dict.update({'sbh':'subahehe'})
data_dict.update({'havs':'hahaha'})

## delete
del data_dict['havs']
print(data_dict)