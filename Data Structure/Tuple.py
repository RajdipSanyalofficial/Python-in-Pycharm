# Tuple is collection of elements which is ordered , immutable, it allows duplicate elements. Like list
# we can assign multiple values in single element

# x=(10,20,30,"Rajdip","WB")
# print(x)
# print(type(x))
#
# print(11 in x)
#
# x1=[10,809,54]
# print(tuple(x1))
# print(type(tuple(x1)))

# a= list(map(int,input("Enter Elements").split()))
# b=[]
# c=[]
# d=[]
#
# for i in a:
#     if i>0:
#         b.append(i)
#     elif i<0:
#         c.append(i)
#     else:
#         d.append(i)
# print(f"+ve is: {b}")
# print(f"-ve is: {c}")
# print(f"zero is: {d}")

# a1=list(map(int,input("Enter Elements: ").split()))
# a2=list(map(int,input("Enter Elements: ").split()))
# s=[]
#
# for i in a1:
#     s.append(i)
#
# for i in a2:
#     s.append(i)
# print(f"{s}")

# a4=list(map(int,input("Enter Elements: ").split()))
# a5=list(map(int,input("Enter Elements: ").split()))
# d1=[]
#
# for i in a4:
#     if i in a5 and i not in d1:
#         d1.append(i)
# print(f"{d1}")
#

# a4=list(map(int,input("Enter Elements: ").split()))
# largest=a4[0]
# second=a4[0]
#
# for i in a4:
#     if i>largest:
#         second=largest
#         largest=i
#     elif i>second and i!=largest:
#         second=i
# print(f"{second}")

# a4=list(map(int,input("Enter Elements: ").split()))
# r=[]
#
# for i in a4:
#     if i not in r:
#         r.append(i)
# print(f"Duplicates: {r}")

z=list(map(int,input("Enter Elements: ").split()))
c=[]

for i in z:
    c.append(i**3)
print(f"Cube elements: {c}")


