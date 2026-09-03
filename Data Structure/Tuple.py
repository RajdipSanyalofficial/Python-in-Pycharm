# Tuple is collection of elements which is ordered , immutable, it allows duplicate elements. Like list
# we can assign multiple values in single element

# We can create tuple by using parenthisis and inside that we are assigning elements in comma
# separated
# We can also create tuple using tuple() and using we can convert any other itearables into tuple

a=(10,20,30,40,"Raju","9999")
print(a)

b=a*3 # using repeatation operator we can use any iterable objects in multiple times
print(b)

c=("Raju" in a) # We can also check all elements present or not inside tuple using in operator
print(c)

d=a.count("Raju")
print(d)
d1=a.index(40)
print(d1)

# How to change tuple?
b1=list(a)
b1.append("Pritam")
b3=tuple(b1)
print(b3)

# insert "Bipasha" at index 3
# remove pritam from tuple
# add 70,80,90, 1000

t=list(a)
t.insert(3,"bipasha")
t1=tuple(t)
print(t1)

d=list(t1)
d.pop(6)
d2=tuple(d)
print(d2)

g=list(d2)
g.extend([70,80,90,100])
g1=tuple(g)
print(g1)
print(a)

n=(g1,a) #adding two tuple
print(n)

