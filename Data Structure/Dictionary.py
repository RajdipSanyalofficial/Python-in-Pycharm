# # Dictionary is a collection of elements that stores in key-value pairs. Elements are ordered,mutable and not allowed duplicate elements
#
# # key -> The key must be unique and immutable
# # value -> The values must be any data type , it may or may not be unique
#
# # 1) using curly braces {} and inside we can specify key and values for elements
# student_dict ={
#     "Id": 16901618087,
#     "NAME": "Rajdip Sanyal",
#     "Location": "Chandannagar",
#     "Roll": 87
# }
# print(student_dict)
# print(type(student_dict))
#
# # 2) by passing the keys and values for elements inside dict() constructor
#
#
# employee_dict= dict(Id="12345", Name="Rajdip Sanyal", Roll=87,State="West Bengal")
# print(employee_dict)
#
# # keys -> returns all the keys from particular dictionary
# print(student_dict.keys())
#
# # values -> returns all the values for that particular keys of dict elements
# print(student_dict.values())
#
# # items() -> Returns all key-value pairs for dict elements
# print(employee_dict.items())
#
# # get() -> returns all value for that particular key which want to access from dict
# print(student_dict.get("Location"))
# print(employee_dict.get("State"))
#
# # iterate dictionary elements in key wise , value wise
#
# for key in student_dict:
#     print(key)
#
# for value in student_dict.values():
#     print(value)
#
# for items in student_dict.items():
#     print(items)
#
#
#
#
#
#
# # occurrance of each item
# s=str(input("Enter String: ")).lower()
# Dict=dict()
#
# for i in s:
#     if i not in Dict:
#         Dict[i]=1
#     else:
#         Dict[i]+=1
# print(Dict)


# i=0
# while i<=10:
#     print(f"My name is Rajdip")
#     i+=1

# s=str(input("Enter name: "))
# n=int(input("how many times? "))
#
# for i in range(1,n+1):
#     print(f"My name is: {s}")

# i=0
# while True:
#     print(i)
#     i+=1
#     if i==7:
#         break



