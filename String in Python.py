# Anagram
# s1=str(input("Enter String"))
# s2=str(input("Enter String"))
#
# if len(s1) != len(s2):
#     print(f"Not Anagram")
# else:
#     for i in s1:
#         if s1.count(i) != s2.count(i):
#             print(f"Not anagram")
#             break
#         else:
#             print(f"Anagram")
#

q1=str(input("Enter String: "))

for i in range(len(q1)):
    for j in range(i+1,len(q1)):
        if q1[i]==q1[j]:
            print("Duplicate Elements: ",q1[i])
            break

