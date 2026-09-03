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

# q1=str(input("Enter String: "))
#
# for i in range(len(q1)):
#     for j in range(i+1,len(q1)):
#         if q1[i]==q1[j]:
#             print("Duplicate Elements: ",q1[i])
#             break

# Duplicate, length, occurance, remove , reverse , plaindrome , vowel consonant, anagram

# m=str(input("Enter String: ")).lower()
# for i in range(len(m)):
#     for j in range(i+1,len(m)):
#         if m[i]==m[j]:
#             print(f"Duplicate: {m[i]}")

# n=str(input("Enter string: "))
# m=""
# for i in range(len(n) -1,-1,-1):
#     m+=n[i]
#
# if m.lower() == n.lower():
#     print(f"Palindrome!!!")
# else:
#     print(f"Not Palindrome!!!")

# n=str(input("Enter string: ")).lower()
# n1=str(input("Enter 2nd string: ")).lower()
#
# if len(n)!=len(n1):
#     print(f"Not Anagram")
#
# for i in n:
#     if n.count(i)!= n1.count(i):
#         print(f"Not anagram")
#     else:
#         print(f"Both are anagarm")

n=str(input("Enter String: "))
v=0
c=0

for i in n:
    if i in "aeiouAEIOU":
        v+=1
    elif i.isalpha():
        c+=1
    print(f"Vowel: {v}")
    print(f"Consonant: {c}")





