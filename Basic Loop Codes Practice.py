# # GCD
# a=int(input("Enter 1st Number: "))
# b=int(input("Enter 2nd Number: "))
#
# while b!=0:
#     a,b=b, a%b
# print(f"Gcd is= {a}")
#
# # a=int(input("Enter 1st Number: "))
# # b=int(input("Enter 2nd Number: "))
# # x,y=a,b
# # while b!=0:
# #     a,b=b, a%b
# #
# # lcm =(x*y)
# # print(f"{lcm}")
#
# #--------------------------------------------------------------------------------------------
# # Sum of digit
# n=int(input("Enter Number: "))
# sum=0
# while n!=0:
#     sum+=n%10
#     n=n//10
#
# Count digit
# count=0
# while n!=0:
#     count+=1
#     n=n//10
# print(f"Sod is: {count}")
#
# # Reverse
# print(f"The reverse is: ")
# temp=n
# while n>0:
#     temp=n%10
#     print(temp,end=" ")
#     n=n//10
#
# #--------------------------------------------------------------------------------------------
# # armstrong
# n=int(input("Enter Number: "))
# temp=n
# d=len(str(n))
# sum=0
#
# while temp>0:
#     digit=temp%10
#     sum+=digit**d
#     temp=temp//10
#
# if sum==n:
#     print(f"{n} is armstrong")
# else:
#     print(f"{n} is not armstrong")
#
# # ---------------------------------------------------------------------------------------------
# # Perfect
# n = int (input("Enter Number: "))
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum+=i
#
# if sum==n:
#     print("{n} is perfect")
# else:
#     print("{n} is not perfect")
#
#
# # ---------------------------------------------------------------------------------------------
# # Prime
# n=int(input("Enter Number: "))
# if n<2:
#     print("{n} is Not Prime")
# else:
#     for i in range(2,n):
#         if n%i==0:
#             print("{n} is Not Prime")
#             break
#
#         else:
#             print("{n} is prime")
#
# # ---------------------------------------------------------------------------------------------
# # Table
# n=int(input("Enter a number for table: "))
# print(f"The table of {n} is - ")
#
# for i in range(1,11):
#     print(f"{n} * {i} ={n*i}")
# print(f"Loop is finished")
#
# # ---------------------------------------------------------------------------------------------
# # Fibonacci
# n=int(input("Enter Number: "))
# a=0
# b=1
# for i in range(n):
#     c=a+b
#     print(a, end=" ")
#     a=b
#     b=c
#
# # ---------------------------------------------------------------------------------------------
# import math
# r=float(input("Enter radius: "))
#
# # s=(4/3)* math.pi * r**3
# s1= math.pi* r**2
# print(f"The area of sphere is {s1}")
#
# cel=float(input("Enter celcius value "))
# fah= (cel* 9/5)+32
# print(f"The farenhite value is: {fah}")
#
# # ---------------------------------------------------------------------------------------------
# # Armstrong
# n=int(input("Enter Number: "))
# temp=n
# d=len(str(n))
# sum=0
# while temp>0:
#     digit=temp%10
#     sum+=digit**d
#     temp=temp//10
# if sum==n:
#     print("{n} is Armstrong")
# else:
#     print("{n} is not Armstrong")
#
# # ---------------------------------------------------------------------------------------------
# # vowel consonant
# ss=str(input("Enter String: "))
# v=0
# c=0
# for i in ss:
#     if i in "AEIOUaeiou":
#         v+=1
#     elif i.isalpha():
#         c+=1
# print(f"The Vowels are: {v}")
# print(f"The consonants are: {c}")
#
# # ---------------------------------------------------------------------------------------------
# # pow(x^n)
# x=int(input("Enter Base: "))
# n=int(input("Enter Power: "))
#
# res=1
# for i in range(1,n+1):
#     res=res*x
# print(f"The value of {x} to the power of {n} is: {res}")
#
# # ---------------------------------------------------------------------------------------------
# # n=int(input("Enter Number: "))
# # #temp=n
# # sum=0
# # #print("The Reverse is: ")
# # while n!=0:
# #     sum+=n%10
# #     #print(temp,end=" ")
# #     n=n//10
# # print(f"The sum of digit is: {sum}")
#
# # ---------------------------------------------------------------------------------------------
# # Factorial
# n1=int(input("Enter Number: "))
# if n1<0:
#     print(f"{n1} is negative , factorial not possible")
# elif n1==0:
#     print(f"factorial of 0 is 1")
# else:
#     fact=1
#     for i in range(1,n1+1):
#         fact=fact*i
# print(f"The Factorial of {n1} is:  {fact}")
#
# # ---------------------------------------------------------------------------------------------
# # # Reverse & palindrome
# r=str(input("Enter String: "))
# z=""
#
# for i in range(len(r) -1,-1,-1): #Reverse
#     z+=r[i]
# # print(f"The Reverse String: {z}")
# if z.lower()==r.lower():
#     print(f"The String is Palindrome!")
# else:
#     print(f"The String is not Palindrome!")
#
# # ---------------------------------------------------------------------------------------------
# # Length and frequency and remove character of string
# l=str(input("Enter String: "))
# term=str(input("Enter item search for: ")) # for frequency/occurance
# c=0 #for length of string and frequency/occurance
# c="" #for remove elements
# for i in l:
#     if i==term: #for frequency/occurance
#     if i!=term: #for remove elements
#         c += i  #for remove elements
#         c+=1    #for length of string and frequency/occurance
# print(f"The Length is: {c}")
# print(f"The occurance of item is: {c}")
# print(f"The final string is: {c}")
#
# # ---------------------------------------------------------------------------------------------
# # anagram
# z1=str(input("Enter String1: ")).lower()
# z2=str(input("Enter String2: ")).lower()
#
# if len(z1)!=len(z2):
#     print(f"Not Anagram!")
#
# for i in z1:
#     if z1.count(i)!=z2.count(i):
#         print(f"Not anagram!")
#     else:
#         print(f"Anagram!")
#
# # ---------------------------------------------------------------------------------------------
# # Leap Year
y=int(input("Enter Year: "))
if (y%400==0) or (y%4==0 and y%100!=0):
    print(f"{y} is Leap Year !")
else:
    print(f"{y} is not Leap Year !")


