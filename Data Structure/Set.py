# Set() -> It is collection of unique values that doesn't allow duplicate elements. Set is unordered
# that's why it cannot be indexed. We can add or remove elements inside set but existing elements
# of set can not be modified.


s={1,2,3,4,5,6,7,8,9}
print(s)
print(type(s))

s1={50,80,90}
s2=s.update(s1)  # For merge two sets or dictionaries use update()
print(s)

s3=s.remove(90) # to remove elements use remove()
print(s)


# set operations

# 1) union () -> It combines unique elements and remove duplicate elements from both sets

A = {30,40,42,50,60}
B= {1,2,5,6,50,60,44}
C = A | B
print(C)

# 2) intersection() -> Returns those elements that is common in both sets

A = {30,40,42,50,60}
B= {1,2,5,6,50,60,44}
C1= A&B
print(C1)

# 3) difference() -> It returns elements that present in first set but not in second set

A = {30,40,42,50,60}
B= {1,2,5,6,50,60,44}
C2= A - B
print(C2)


list = [10,10,60,60,30,50,9,9]
b=set(list)
print(b)






