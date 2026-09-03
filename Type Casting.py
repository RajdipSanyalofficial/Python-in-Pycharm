# Type Casting is a mechanism that allows to convert the value of one data type into another
# data type weather by python interpreter automatically or manually by user. It is also known as
# type conversion.
# It is mostly used when we need to perform operations in two different data types


# 1) Implicit Type casting

# It is automatically done by python interpreter to convert the value of one data type into another data type
# without any inconvenience of user.
# In case of implicit type casting the value of low precision data type is converted to value of high precision
# data type to avoid the data loss

a=20
b=10.0
c=a+b
print(c) #30.0
print(type(c)) #type float

# 2) Explicit Type Casting

# It is manually done by programmers with the help of python's in build methods like int(),float(),bool(),str()
# to convert the value of data type into value of another data type
# In case of explicit type casting the value of high precision data type is converted to value of
# low precision data type.
# In case of explicit type casting there is a huge possibility of data loss to convert the value of
# high precision to the value of low precision data type


a1=90
a2=float(a1)
print(a2) #90.0 -> float
print(type(a2)) # float

s=90
s1=str(s)
print(s1) # "90" -> Str
print(type(s1)) #str

x="55"
x1=int(x)
print(x1) #55 -> int
print(type(x1)) #int

d=0
d1=bool(0)
print(d1) # False
print(type(d1)) #bool

f=99999
f1=bool(f)
print(f1) #True
print(type(f1)) #bool




