# conditional statements are used to execute the block of code based on some conditions that
# evaluates true or false.
# It also determines the controlling flow and decision making of block of code based on some specific values
# or conditions.

# 1) if statement
# if statement is used to check the condition and executes the corresponding block of code
# if the condition is true

age=int(input("Enter age: "))

if age>=18:
    print(f"You are eligible for voting!!!")

# 2) if-else statement
# If else statement provides alternative block of code and that also executes when the condition is not true.
price=int(input("Enter price: "))
if price >50:
    print(f"Price is too high!!!")
else:
    print(f"Yes now you can buy😁")

# 3) if-elif else
# This statement is used to check for multiple statement at a time and executes specific block of code
# if the condition is true

value=int(input("Enter value: "))
if value>0:
    print(f"Positive!!!")
elif value<0:
    print(f"Negative!!!")
else:
    print(f"Zero!!!")

# 4) nested if else
# nested if else means the if else statement that is place inside another if else is known as nested if else
# It is used in complex descion making and also used to check multiple conditions that depend on each other






