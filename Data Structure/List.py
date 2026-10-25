# List is collection of elements which is ordered, mutable and allows duplicate elements. It is used
# to store multiple elements in single variable

# # a=[10,20,30,40]
# # print(a)
# # print(type(a))
# #
# # b=["abc","def","ghijk"]
# #
# # # append
# # #1st list.append(2nd list)
# # # a.append(b)
# # # print(a) # [10, 20, 30, 40, ['abc', 'def', 'ghijk']]
# # #
# # # print(a[2]) #30
# # # print(a[4]) # ['abc', 'def', 'ghijk']
# # # print(a[4][2]) # ghijk
# # #
# # # a[0]="Rajdip"
# # # print(a) # ['Rajdip', 20, 30, 40, ['abc', 'def', 'ghijk']]
# # #
# # # # list methods
# # #
# # # print(a[::-1]) # reverse list
# # # a.reverse()
# # # print(a)
# # #
# # # b.sort()
# # # print(b)
# # #
# # # # insert()
# # # a.insert(3,"Pritam")
# # # print(a)
# # # a.pop(2)
# # # a.pop()
# # # print(a)
# #
# # c=a.count(20)
# # print(c)
# # a.append(b)
# # print(a)
# # a.extend(b)
# # print(a)
# #
# # print(a) # [10, 20, 30, 40, ['abc', 'def', 'ghijk'], 'abc', 'def', 'ghijk']
# #
# # print(a.count("abc"))
# #
# # a.insert(1,"abc")
# # print(a)
# # print(a.count("abc"))
# # print(a.index("abc"))
# # w=a.pop(4)
# # print(w)
# # print(a)
# # w1=a.pop(4)
# # print(a) #[10, 'abc', 20, 30, 'abc', 'def', 'ghijk']
# # w2=a.index("def")
# # print(w2)
# #
# # s=[a for a in range(1,11) if a%2!=0]
# # print(s)
# #
# # ss=[z**3 for z in range(1,21)]
# # print(ss)
# #
# #
# # xx=["Rajdip","Pritam","Paritosh"]
# # x2=[r.upper() for r in xx]
# # print(x2)
# #
# # d=len(a)
# # print(d)
# #
# # name=["Raj","Dip","Partha","Pritam"]
# # age=[20,30,40,55]
# #
# # q= list(zip(name,age))
# # print(q)
# #
# #
# # h=[60,50,40,30,20,10,5,4,3,2,1]
# #
# # h1=[w**3 for w in h ]
# # print(h1)
# #
# # h2=[f**4 for f in range(1,51)]
# # print(h2)
# #
# student={
#     "Id": [10,20,30,40],
#     "Name":["Raj","Dip","Partha","Pritam"],
#     "Age":[27,30,40,55]
# }
#
# for i in student.items():
#     print(f"The items are: {i}")
#
# for a in student.values():
#     print(f"Values are: {a}")
#
# for b in student.keys():
#     print(f"{b}")
#
#
#
# def names(*args):
#     for a in args:
#         print(f"Names are: {a}")
#
# names("Raju","Pritam")
#
# def abc(**kwargs):
#     for key,value in kwargs.items():
#         print(f"Key is: {key}, Values are: {value}")
#
# abc(Name="Rajdip",Age=27,State="WB")
#
#
# Student=dict(Name="Raj",Age=27,State="WB")
# print(Student)
#
#
# def division(a,b):
#     return a/b
#
# x=division(b=10,a=20) #req
# y=division(10,20) #key
#
# print(x)
# print(y)

nums=[10,20,30,40]
n1= [e**2 for e in nums]
print(n1)

n2=[z**4 for z in range(1,6)]
print(n2)

n3=[f for f in nums if f%2==0]
print(n3)

