# Function is a set of instruction which is used to perform some particular task. It takes some input,performs some operations and produces output.

def is_even(n):
    if n%2!=0:
        print("ODD")
    else:
        print("EVEN")
#is_even(3)

for i in range(1,16):
    is_even(i)


# What is parameter?
#A parameter is a variable declared in the function definition that receives values (arguments) when the function is called.
# The function name and number of arguments in calling fun and called fun must be same
# By mistake if we add more arguments rather than it is specified to accept then it is returned an error.

# Return statement
# The return statement is used to send a value or expression from the called function back to the calling function.
# It also terminates the execution of the function immediately.





# 1) Default Parameter
# Dp is used to initialize function parameters with default values.
# If no argument is provided during the function call, Python uses the default value automatically.

def power(c,d):
    print(c**d)

power(3,4)

def power(c=2,d=2):
    print(c**d)

power(3,) #Default Parameter


def power(c=3,d=3):
    print(c**d)

power() #Default Parameter




# map()
# It is used to apply a specified function to every element of an iterable (such as a list, tuple, or set)
# and returns a map object containing the transformed values.

m=list(map(lambda x:x**3,[1,2,3,4,5,6,7,8,9]))
print(m)


# filter()
# It applies a specific condition to the elements of iterable objects like list tuple set dict and
# returns a filtered object containing those elements those can satisfy the particular condition
nums=[1, 2,3 , 4,5,6,7,8,9]
x=list(filter(lambda a:a%2!=0,nums))
print(x)

# reduce()
# It applies a special condition to the items of iterable objects like list,tuple,set,dict
# and converting multiple elements to single element means reducing from multipole values to
# single values that is reduce()
# It is available inside functools module

from functools import reduce
w= reduce(lambda b,c:b+c,[1,2,3,4,5,6])
print(w)

# we need to convert list object only for map and filter not for reduce

# Required Argument -> that can pass through the function in a correct positional order
def names(abc):
    print(f"Hello- {abc}")

names("Bipasha")

# default argument

def df(name="Raju"):
    print(f"Hello {name}")

df() # default parameter is used
df(name="Chandrani") # we are passing argument for that parameter name

# keyword argument

def divide(a,b):
    return a/b

a=divide(a=10,b=20) #keyword
b=divide(10,20)
print(a)
print(b)

# def names(*args):
#     for i in args:
#         print(i)
#
# names("Rajdip",27)

b=10
def vc():
    a=20
    print(a) #20
    print(b) #10

vc()
print(a)
print(b) #10

nums=(1,2,3,4,5,6,7,8,9,1,32,2,3,2314)

# map()

b=list(map(lambda x:x**2,nums))
print(b)


# filter()

c=list(filter(lambda y: y%2!=0,nums))
print(c)
c2=list(filter(lambda v: v%2==0,nums))
print(c2)

# reduce()
d=reduce(lambda c,d:c+d,nums)
print(d)


x=["Raju","Sujit","Pritam","Dip"]
x1=[a.capitalize() for a in x]
print(x1)






