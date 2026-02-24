#operasi komparasi

#<,>,<=,>=,==,!=,is,is not

a=5
b=7

print("===Lebih Dari (>)===")
hasil=a > 4
print( a,'>',4, '=',hasil)
hasil=b > 8
print( b,'>',8, '=',hasil)
hasil= b > 7
print( b,'>',7, '=',hasil)
print(' ')
print("===Kurang Dari (>)===")
hasil=a < 4
print( a,'<',4, '=',hasil)
hasil=b < 8
print( b,'<',8, '=',hasil)
hasil= b < 7
print( b,'<',7, '=',hasil)
print(" ")
print("===Lebih Dari Sama dengan (>=)===")
hasil= a >= 8
print( a,'>=',8, '=',hasil)
hasil= b >= 6
print( b,'>=',6, '=',hasil)
hasil= b >= 7
print( b,'>=',7, '=',hasil)
print(" ")
print("===Kurang Dari Sama dengan (<=)===")
hasil= a <= 8
print( a,'<=',8, '=',hasil)
hasil= b <= 4
print( b,'<=',4, '=',hasil)
hasil= b <= 7
print( b,'<=',7, '=',hasil)
print(" ")
print("=== Sama dengan (=)===")
hasil= a == 5
print(a,'==',5,'=',hasil)
hasil= a == 6
print(a,'==',6,'=',hasil)
print(" ")
print("=== Tidak Sama dengan (=)===")
hasil= a != 5
print(a,'!=',5,'=',hasil)
hasil= a != 6
print(a,'!=',6,'=',hasil)
print(" ")
#'is'sebagai object identity
#gampangane kyok bandingno object'e kyok variabel gampangane tapi orak variabel
x=5
y=5
print("=== object identity (is)===")
print ("nilai x : ",x,'|id : ',hex(id(x)))
print ("nilai x : ",y,'|id : ',hex(id(y)))
#nah iki mbandeng no seng nduwur iki
hasil= x is y
print ("x is y : ",hasil)
x=5
y=7
print ("nilai x : ",x,'|id : ',hex(id(x)))
print ("nilai x : ",y,'|id : ',hex(id(y)))
#nah iki mbandeng no seng nduwur iki
hasil= x is y
print ("x is y : ",hasil)
x=5
y=5
print(" ")
print("=== object identity not (is not)===")
print ("nilai x : ",x,'|id : ',hex(id(x)))
print ("nilai x : ",y,'|id : ',hex(id(y)))
#nah iki mbandeng no seng nduwur iki
hasil= x is not y
print ("x is y : ",hasil)
x=5
y=7
print ("nilai x : ",x,'|id : ',hex(id(x)))
print ("nilai x : ",y,'|id : ',hex(id(y)))
#nah iki mbandeng no seng nduwur iki
hasil= x is not y
print ("x is y : ",hasil)