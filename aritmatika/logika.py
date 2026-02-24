#operasi logika

# not , or ,and , xor
a= True
b= not a
print("===NOT===")#lawane gamppangane
print("data a :",a)
print("------------NOT")
print ("data b :",b)
print("===AND===")#tek salah siji false,dadine false
a= True
b= False
c=a and b
print(a,'AND',b,' =',c)
a= False
b= True
c=a and b
print(a,'AND',b,' =',c)
a= False
b= False
c=a and b
print(a,'AND',b,'=',c)
a= True
b= True
c=a and b
print(a,'AND',b,'  =',c)
print(" ")
print("===OR==")#tek salah sijine true,dadi true
a= True
b= False
c=a or b
print(a,'OR',b,' =',c)
a= False
b= True
c=a or b
print(a,'OR',b,' =',c)
a= False
b= False
c=a or b
print(a,'OR',b,'=',c)
a= True
b= True
c=a or b
print(a,'OR',b,'  =',c)
print(" ")
print("===XOR==")#kudune ono true siji tok,tek true ne 2 keitung false
a= True
b= False
c=a ^ b
print(a,'XOR',b,' =',c)
a= False
b= True
c=a ^ b
print(a,'XOR',b,' =',c)
a= False
b= False
c=a ^ b
print(a,'XOR',b,'=',c)
a= True
b= True
c=a ^ b
print(a,'XOR',b,'  =',c)
#wes