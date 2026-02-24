data = "ini adalah string"
print(data)
print(type(data))

# 1. cara membuat string

'''
    1. dengan menggunakan single quote '...'
    2. dengan menggunakan double quote "..."
'''
#single quote iku tanda iki (')
#double quote iku tanda iki (")

data = 'Menggunakan single quote'
print(data)

data = "Menggunakan double quote"
print(data)

print('"Halo, apa kabar?"')
print("'Halo, apa kabar?'")
print("ini adalah hari jum'at")

# 2. Menggunakan tanda \

# membuat tanda ' menjadi string
print('mari shalat jum\'at')
print('g\'day, isn\'t it?')
print('aku sedang ma\'had')

# backlash
print("C:\\user\\Ucup")
print("17\\11\\24")
#iki tek pengen muncolno gares mireng e gowo gares mireng 2 kuddune (\\)

# tab
print("ucup\t\t\totong, semakin jauhan")

# backspace
print("ucup \botong, jadi deketan"  )
#iki kanggo ngapos mburine

# newline
print("baris pertama.\nbaris kedua.") # LF -> line feed -> unix, macos, linux
print("baris pertama.\rbaris kedua.") # CR -> carriage return -> commodore, acorn, lisp 
print("baris pertama.\r\nbaris kedua.") # CRLF -> line feed carriage return -> dipakai oleh windows

# 3. String literal atau raw

# hati-hati
print('C:\new folder') # akan salah pathnya

# menggunakan raw string
print(r'C:\new folder')
#r = Raw ben aman tek nggowo gares mireng (\)

# multiline literal string
print("""
Nama : Ucup
Kelas : 3 SD   
""")

# multiline literal string dan RAW
print(r"""
Nama : Ucup
Kelas : 3 SD\new normal 
Website : www.ucup.com/newID
""")