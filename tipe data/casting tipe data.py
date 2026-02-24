data_int   =88
data_float =float(data_int)
data_str   =str(data_int)
data_bool  =bool(data_int)

print("============INTEGER=============")
print("data :", data_int , "type : ",type(data_int))#bulatnone ngo ngisor makno
print("data :", data_float , "type : ",type(data_float))
print("data :", data_str , "type : ",type(data_str))
print("data :", data_bool , "type : ",type(data_bool))#tek ongkone orak 0 berarti true

data_float  =88.2
data_int   =int(data_float)
data_str   =str(data_float)
data_bool  =bool(data_float)

print("============FLOAT=============")
print("data :", data_float , "type : ",type(data_float))
print("data :", data_int , "type : ",type(data_int))#bulatnone ngo ngisor makno
print("data :", data_str , "type : ",type(data_str))
print("data :", data_bool , "type : ",type(data_bool))

data_str   ="10"
data_int   =int(data_str) #string harus ongko
data_float =float(data_str)#string harus ongko
data_bool  =bool(data_str)#kudune gaono isine nek stringe tek pengen dadi false

print("============STRING=============")
print("data :", data_str , "type : ",type(data_str))
print("data :", data_float , "type : ",type(data_float))
print("data :", data_int , "type : ",type(data_int))#bulatnone ngo ngisor makno
print("data :", data_bool , "type : ",type(data_bool))

data_bool  =False;
data_int   =int(data_bool)
data_float =float(data_bool)
data_str   =str(data_bool)

print("============BOOL=============")
print("data :", data_bool , "type : ",type(data_bool))
print("data :", data_str , "type : ",type(data_str))
print("data :", data_float , "type : ",type(data_float))
print("data :", data_int , "type : ",type(data_int))#bulatnone ngo ngisor makno
