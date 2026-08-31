# Set() -> It is collection of unique values


# s={1,2,3,4,5,6,7,8,9}
# print(s)
# print(type(s))





# set operations

# 1) union () -> It combines unique elements and merge both sets

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






