# n=int(input("Enter Number: "))
# if n<0:
#     print(f"Negative number")
# elif n==0:
#     print(f"Fact of 0 is 1!")
# else:
#     fact=1
#     for i in range (1,n+1):
#         fact=fact*i
# print(f"Factorial of {n} is {fact} ")

# a=int(input("enter number: "))
# if a<2:
#     print(f"Not Prime!!!")
# else:
#     for i in range(2,a):
#         if a%i==0:
#             print(f"Not prime!!!")
#             break
#         else:
#             print(f"Prime Yaaaaaa !!!!!")

# n=int(input("Enter Number: "))
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum+=i
#
# if sum==n:
#     print(f"Num is Prefect")
# else:
#     print(f"Not Perfect!!!")


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
#     print(f"{n} is Armstrong!!")
# else:
#     print(f"{n} is not armstrong!!!!")

# prime and perfect number
# n=int(input("Enter Number: "))
# if n<2:
#     print(f"Not Perfect!!!")
# else:
#     for i in range(2,n):
#         if n%i==0:
#             print(f"Not Prime!!!")
#             break
#         else:
#             print(f"The number is prime!!!")

# n=int(input("Enter Number: "))
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum+=i
# if sum==n:
#     print(f"Prefect!!!")
# else:
#     print(f"Not Perfect!!!")

# Armstrong
# n=int(input("Enter Number: "))
# temp=n
# d=len(str(n))
# sum=0
#
# while temp>0:
#     digit=temp%10
#     sum+=digit**d
#     temp=temp//10
# if sum==n:
#     print(f"armstrong")
# else:
#     print(f"Not Armstrong!!!")

# Fibonacci
# n=int(input("Enter Number: "))
# a=0
# b=1
# for i in range(n):
#     print(f"The Fibonacci Numbers are: {a}")
#     c=a+b
#     a=b
#     b=c

# yr = int(input("Enter Year: "))
# if (yr%400==0) or (yr%4==0 and yr%100!=0):
#     print(f"Yes It's Leap Year!!!")
# else:
#     print(f"You are wrong, Not Leap Year!!!")

# n=int(input("Enter Number: "))
# temp=n
# d=len(str(n))
# sum=0
#
# while temp>0:
#     digit=temp%10
#     sum+=digit**d
#     temp=temp//10
# if sum==n:
#     print(f"{n} is armstrong")
# else:
#     print(f"{n} is not armstrong")

# m=int(input("Enter Number: "))
# print(f"The Table of {m} is: ")
#
# for i in range(1,11):
#     print(f"{m} * {i} = {m*i}")

# m=int(input("Enter lower range: "))
# n=int(input("Enter upper range: "))
#
# for i in range(m,n+1):
#     if i%2==0:
#         print(f"{i} is Even")
#     else:
#         print(f"{i} is Odd")

# m=int(input("enter lower: "))
# n=int(input("enter upper: "))
#
# for i in range(m,n+1):
#     print(f"Number is: {i} , Square is: {i**2}, Cube is: {i**3}")

# n=int(input("enter Number: "))
# sum=0

# while n!=0:
#     sum+=n%10
#     n=n//10
# print(f"Sod is: {sum}")
#
# n=int(input("Enter Number: "))
# count=0
#
# while n>0:
#     count+=1
#     n=n//10
# print(f"COD is: {count}")
#
#
# n=int(input("Enter Number for reverse: "))
# temp=n
# print(f"The Reverse of {n} is: ")
# while n!=0:
#     temp=n%10
#     print(temp,end=" ")
#     n=n//10
