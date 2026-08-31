# # Generated from: Python Introduction.ipynb
# # Converted at: 2026-08-17T20:20:21.688Z
# # Next step (optional): refactor into modules & generate tests with RunCell
# # Quick start: pip install runcell
#
# x= 10
#
# y=20
#
# z= x+y
#
# print(z)
#
# print("Hello World")
# print(5)
# print("Bye")
# print(17*13)
#
# """
# Hey, Please don't remove this line
# Course: python introduction
#
# """
# print("Hey I am a \"good boy\"\nand this viewer is also a good boy/girl")
#
# print("this is a print statement")
#
# print("hey", 6, 7, sep="-", end="009\n")
# print("Hi")
#
# a = 1
# print(a)
# a
#
# b = "Hello"
# print(b)
#
# a1 = 9
# print(a+a1)
#
# print("the type of a is:", type(a))
#
# type(a)
#
# c = complex(8, 2)
# c
#
# type(c)
#
# list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]
# print(list1)
#
# list1
#
# tuple1 = (8, 2.3, [-4, 5], ["apple", "banana"])
# print(tuple1)
#
# type(list1)
#
# type(tuple1)
#
# dict1 = {"name": "shakshi", "age": 20, "canVote": True}
# print(dict1)
#
# type(dict1)
#
# print(15//6)
#
# print(5%3)
#
# print(5**3)
#
# a = 10
# b = 3
#
# print("The value of", a, " + ", 3, "is: ", a + b)
# print("The value of", a, " - ", 3, "is: ", a - b)
# print("The value of", a, " * ", 3, "is: ", a * b)
# print("The value of", a, " / ", 3, "is: ", a / b)
# print("The value of", a, " // ", 3, "is: ", a // b)
# print("The value of", a, " % ", 3, "is: ", a % b)
# print("The value of", a, " ** ", 3, "is: ", a ** b)
#
# a = "1"
# b = "2"
# print(a + b)
#
# a = 1
# b = 2
# print(a + b)
#
# a = "1"
# b = "2"
# print(int(a) + int(b))
#
# # explicit typecasting
#
# string = "15"
# number = 7
# string_number = int(string)
# sum = number + string_number
# print("The Sum of Both The Numbers Are: ", sum)
#
# # implicit typecasting
#
# c = 1.9
# d = 8
# print(c + d)
#
# e = input("enter your")
# print("My name is", e)
#
# x = input("enter first number: ")
# y = input("enter second number: ")
# print(x + y)
#
# 12+100
#
# name = "Rajdip"
# friend = "Rahul"
# anotherfriend = 'Shuvra'
#
# print("Hello " + name)
#
# print(name[0])
#
# name[0]
#
# for charecter in (name, friend, anotherfriend):
#     print(charecter)
#
# names = "Shuvra,Rohan"
# print(names[0:6])
#
# print(len(names))
#
# names = "Shuvra,Rohan"
# print("Full string:", names)
# print("Character count:", len(names))
# print("Character positions:", end=" ")
# for i, char in enumerate(names):
#     print(f"{char}[{i}]", end=" ")
#
# fruit = "Mango"
# len1 = len(fruit)
# print(len1)
# print(fruit[1:4])
# print(fruit[:4])
# print(fruit[0:-3])
# print(fruit[-3:-1])
#
# nm = "Shuvra"
# print(nm[-4:-2])
#
# a = "shuvra!!!!!!!!!!!!!!!!!!shuvra"
# len(a)
#
# print(a.upper())
#
# print(a.lower())
#
# print(a.rstrip("!"))
#
# print(a.replace("shuvra", "john"))
#
# print(a.split(" "))
#
# blogheading = "introduction to python"
# print(blogheading.capitalize())
#
# str1 = "welcome to the python program"
# print(len(str1))
# print(len(str1.center(50)))
#
# str1 = "welcome to the python program"
# print(len(str1.center(50)))
#
# str1 = "welcome to the python program !!!"
# print(str1.endswith("!!!"))
# print(str1.startswith("welcome"))
#
# str1 = "welcome to the python program !!!"
# print(str1.endswith("to", 4, 10))
#
# str1 = "He's name is Rajdip. He is an honest and hardworking student"
# print(str1.find("is"))
#
# print(str1.index("name"))
#
# str1 = "welcome to the python program"
# print(str1.isalnum())
#
# str1 = "welcome"
# print(str1.isalpha())
#
# str1 = "hello world"
# print(str1.islower())
#
# str1 = "hello world"
# print(str1.isupper())
#
# str1 = "wish you a merry christmas\n"
# print(str1)
#
# print(str1.isprintable())
#
# str1 = "          "
# print(str1.isspace())
#
# str2 = " "
# print(str2.isspace())
#
# str1 = "World Health Organisation"
# print(str1.istitle())
#
# str1 = "Python is an Interpreted Language"
# print(str1.startswith("Python"))
#
# str1 = "Python is an Interpreted Language"
# print(str1.swapcase())
#
# str1 = "His name is Rajdip. He is an honest and hardworking student"
# print(str1.title())
#
# # If Else condition
#
# a = int(input("Enter your age"))
# print("Your age is:", a)
#
# print(a>18)
# print(a<=18)
# print(a==18)
# print(a!=18)
# if(a>18):
#     print("You can drive")
#     print("Yes")
# else:
#     print("You cannot drive")
#     print("No")
#
# appleprice = 210
# budget = 200
# if (appleprice <= budget):
#     print("Alexa, add 1 kg of apples to the cart")
# else:
#     print("Alexa, do not add apples to the cart")
#
# appleprice = 10
# budget = 200
# if (budget - appleprice > 50):
#     print("Alexa, add 1 kg of apples to the cart")
# elif (budget - appleprice > 70):
#     print("it's okay you can buy")
# else:
#     print("Alexa, do not add apples to the cart")
#
# num = int(input("Enter the value of num: "))
# if (num < 0):
#     print("number is negative")
# elif (num == 0):
#     print("Number is zero")
# elif (num == 999):
#     print("Number is special")
# else:
#     print("Number is positive")
# print("I am Happy")
#
# num = 18
# if (num < 0):
#     print("number is negative")
# elif (num > 0):
#     if (num <= 10):
#         print("number is between 1-10")
#     elif (num > 10 and num <= 20):
#         print("number is between 11-20")
#     else:
#         print("number is greater than 20")
# else:
#     print("number is zero")
#
# import time
# timestamp = time.strftime('%H:%M:%S')
# print(timestamp)
# timestamp = time.strftime('%H')
# print(timestamp)
# timestamp = time.strftime('%M')
# print(timestamp)
# timestamp = time.strftime('%S')
# print(timestamp)
#
# import os
#
# print("Hello World")
# os.system("python --version")
#
# x = int(input("Enter the value of x: "))
# match x:
#     case 0:
#         print("x is zero")
#     case 4:
#         print("case is 4")
#     case _ if x!=90:
#         print(x, "is not 90")
#     case _ if x!=80:
#         print(x, "is not 80")
#     case _:
#         print(x)
#
# name = "shuvra"
# for i in name:
#     print(i)
#     if (i == 'h'):
#         print("this is something special")
#
# colors = ["Red", "Green", "Blue", "Yellow"]
# for color in colors:
#     print(color)
#     for i in color:
#         print(i)
#
# for k in range(5):
#     print(k + 1)
#
# for k in range(1, 11):
#     print(k)
#
# for k in range(1, 12, 2):
#     print(k)
#
# i = 0
# while(i<=3):
#     print(i)
#     i = i + 1
# print("done with the loop")
#
# i = int(input("Enter the number: "))
# while(i<=38):
#     i = int(input("Enter the number: "))
#     print(i)
# print("done with the loop")
#
# count = 5
# while(count > 0):
#     print(count)
#     count = count - 1
# else:
#     print("done with the loop")
#
# for i in range(12):
#     print("5 X", i+1, "=", 5 * i+1)
#     if(i==10):
#         break
# print("Loop is finished")
#
# for i in range(12):
#     if(i==10):
#         break
#     print("5 X", i+1, "=", 5 * (i+1))
#
# print("Loop is finished")
#
# for i in range(12):
#     if(i==10):
#         print("skip the iteration")
#         continue
#     print("5 X", i, "=", 5 * i)
#
# i = 0
# while True:
#     print(i)
#     i = i + 1
#     if(i%10 == 0):
#         break