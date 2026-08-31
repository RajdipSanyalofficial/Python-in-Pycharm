# Generated from: Python Beginners Level.ipynb
# Converted at: 2026-08-17T20:19:55.155Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

# <a id='1'></a><center> <h3 style="background-color:orange; color:white" ><br>Python Basics<br></h3>


# What is your name! print your name!
# Only use one print function

print("Shuvra Prakash")

print("Rajdip Sanyal")

# * `()` <= `Parentheses`
# * `''` <= `Single Quotes`
# * `""` <= `Double Quotes`
# * `\n` <= `New_line `
# * `#` <= `Used to comment inside code`


# define variables named as with values: mukesh=7, z=6, rohan=5, longitude=4

mukesh = 7
z = 6
rohan = 5
longitude = 4

a=7
z=6
raju=5
longitude1=4

print(a)


# print required variable
# output - 5

# print(rohan)
rohan

# Variable Assignment:
# **`Variable_Name = Value`**
#
# Variables Naming Rules:
# * `Python is case-senstive` => x=5 is different from X=5 (one is lowe and other is upper case)
# * `var name can't start with special character except underscore(_)` => _X = 7 is `valid`, @X = 7 is `invalid`
# * `var name can't start with number` => 9X = 7 is `invalid`, X9 = 7 is `valid`
# * can't use `keywords` as a variable name
#     *


# # **`Declaring a Variable`** <br>
#


# declare 4 variables with values as: ur_age 21,ur_weight 50.6, ur_first_name = 'Mukesh',ur_last_name = "Kumar"

ur_age = 21
ur_weight = 50.6
ur_first_name = 'Mukesh'
ur_last_name = "Kumar"

# # **`Data Type(Type of variable)`**


# | Name | Type | Description |
# | ---- | ---- | ----|
# |Integers | int | Integer number, like 34,-56 ...|
# |Float | float | Decimal number, like 3.4,-5.6 ...|
# |String| str | Ordered sequence of characters, like 'your name' |
# |Boolean |bool |Logical values indicating True or False only |


# print type of ur_age,ur_weight,ur_first_name,ur_last_name variables

print("Type of ur_age:", type(ur_age))
print("Type of ur_weight:", type(ur_weight))
print("Type of ur_first_name:", type(ur_first_name))
print("Type of ur_last_name:", type(ur_last_name))

# print values of ur_age,ur_weight,ur_first_name,ur_last_name variables

print("Value of ur_age:", ur_age)
print("Value of ur_weight:", ur_weight)
print("Value of ur_first_name:", ur_first_name)
print("Value of ur_last_name:", ur_last_name)

# make 2 variables with values as: ur_first_name 'Mukesh',ur_last_name'Mukesh'

ur_first_name = 'Mukesh'
ur_last_name = 'Mukesh'

# make a variable TrueOrFalse which will have comparison of variables ur_last_name == ur_first_name

TrueOrFalse = (ur_last_name == ur_first_name)



# define a variable name "x" and assign value 777 and print it

x = 777
print(x)

# * To view some data on screen, python have `print` function
#     * Using `print` function we can control view on output screen
#




# `Operators`: Symbols that represent mathematical or logical tasks
#
# Example:<br>
# `700` `+` `77`<br>
# * `+` <= Operator
# * `700` & `77` <= Operands
#


# Initialize variables [x,y,z,zz] with values
## x as 7 =>int ,
## y as 77 =>int,
## z as 77.7 => float,
## zz as 'Hi' => string

x = 7      # integer
y = 77     # integer
z = 77.7   # float
zz = 'Hi'  # string

# # **`Arithmetic Operators`**


# add x and z

x + z

# subtract z and y

z - y

# Multiply x and z

x * z

# Exponent (raise the power or times) x times z

x ** z

# division on x and z

x/z

# `//` => divides and returns integer value of quotient
# * It will dump digits after decimal


# floor division(ignores decimal) on x and z (gives quotient)

x//z

# Modulo(gives remainder) on x and z

x % z

# # **`Comparison Operators`**


# comapre and see if x is less then z
# can use '<' symbol

x < z

# check the type of above comaprison where it says comapre and see if x is less then z

type(x < z)

# * `Bool` => takes two values, either `True` or `False`


# compare and see if x is less then or equall to z
# can use '<=' symbol

x <= z

# compare and see if x equall to z
# can use '==' symbol

x == z

# comapre and see if x is greater than z
# can use '>' symbol

x > z

# compare and see if x is greater than or equall to z
# can use '>=' symbol

x >= z

# compare and see if x is Not equall to z
# can use '!=' symbol

x != z

# # **`Logical Operators`**


# compare if 108 is equall to 108, 21 is equall to 21 using logical and
# equall to => '=='
# logical and => and

print(108 == 108 and 21 == 21)

# in and both condition must be True to get a True

# how above condition can give False as output show all those conditions

print(not(108 == 108 and 21 == 21))

# compare if 108 is equall to 108, 21 is equall to 11 using logical or
# equall to => '=='
# logical or => or

print(108 == 108 and 21 == 11)

# in or Only one condition need to be True to get a True

# this is for you to understand it
(108 == 108) or (21 == 11) or (108 <= 11)



# # **`if`--- `else`** => to handle single condition <br>
# # **`if`--- `elif`--- `else`** => to handle Multiple condition


# `Observe in Python code:`
# * `if` => statement in python
# * `else` => statement in python
# * `:` => colon => denotes start of if block i.e. any line written after colon belong to if condition
# * `....` => see then as indentation i.e. 4 spaces => indentation indicates all code belong to only if and then another indentation indicates code for only else block


# make variable with value as : money 100000

money = 100000

# see output of money > 2000

print(money > 2000)

# assign money variable value of 10000
##### say you have this much ammount in your account

money = 10000

# start of if condition
# if money is greater then 1000 which is data science course fee

if money > 1000:
    print("data science course fee")

# if money > 1000 is false i.e. you have less money then 1000 in your account then else will work for now only if is working

if money < 1000:
    print("you have less money then 1000")

# take a test_score variable with 80 in it.

test_score = 80

# if test_score greater then 80 then print A grade

if test_score > 80:
    print("A grade")

# elif test_score greater then 60 and less then 80 print B grade

elif test_score > 60 and test_score <= 80:
    print("B grade")

# else print Nothing for you

else:
    print("Nothing for you")



# # **`Python Loops`**


"""
for iterating_variable in sequence:
    statement(s)
"""

for iterating_variable in range(10):
    print(iterating_variable)

# print 'I love sports' 10 times using for loop

for _ in range(10):
    print("I love sports")

# `10` => `stoping criteria` of, for loop


# * `in` => keyword
# * `sequence` => on which to itterate
# * `:` => colon , start of for loop


# `!=` = not equall to => `behaves as a stoping criteria`


# Syntax of while loop
"""
while comparison:
    statements(s)
"""

# while loop

# save 0 in variable number

# print till 10 using while loop


number = 0  # Initialize number with 0

while number <= 10:
    print(number)
    number += 1

# * Initialized variable `number = 0` and then increment it's value in each iteration
# * Loop will only continue to run only if value is less than 10


# # **`Type of Jump Statements`** <br>
# `Break Statement`
# `Continue Statement`


# # **`Break Statement`**
#


# example that uses break statement in a for loop

# Define a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Iterate over the numbers using a for loop
for number in numbers:
    if number > 5:
        break  # Exit the loop if number is greater than 5
    print(number)


# take range(10) and print 'The number is' + value
# break when num equals 5

for number in range(10):
    print('The number is', number)
    if number == 5:
        break

# # **`Continue Statement`**
#


# Using same `for loop program` as in Break Statement section above
# Use a continue statement rather than a break statement
# take range(10) and print 'The number is' + value
# continue when num equals 5

for number in range(10):
    if number == 5:
        continue
    print('The number is', number)



# # **`String Manipulation`**


string_ = '' or "" or """ """

# define a string variable with "We are creating next generation data science eco-system at Kolkata"

str = "We are creating next generation data science eco-system at Kolkata"

# Find length of string including spaces

print("Length of the string including spaces:", len(str))

# Access characters in a string with indexing i.e string[0]

print(str[0])

# Access characters with negative indexing i.e string[-1]

print(str[-1])

# # String Slicing


# select string from first to 6th element i.e string[:6]

print(str[:6])

# select string from 7th to negative 10th element i.e string[7:-10]

print(str[7:-10])

# Count of a particular `character` in a string


print(str.count('e'))

# Count of a particular `sub-string` in a string


print(str.count('at'))

# Find a substring in string using `find` and `index` function


# .find() => if present it will return starting index, not found then it will return -1
# .index() => if present it will return starting index, not found then it will give error

print(str.find('are'))
print(str.index('at'))

### Checking whether string `startswith` or `endswith` a particular substring or not

starts_with_we_are = str.startswith("We are")
print("Starts with 'We are':", starts_with_we_are)

starts_with_creating = str.startswith("creating")
print("Starts with 'creating':", starts_with_creating)

ends_with_kolkata = str.endswith("Kolkata")
print("Ends with 'Kolkata':", ends_with_kolkata)

ends_with_science = str.endswith("science")
print("Ends with 'science':", ends_with_science)




### Converting string to upper case ###

print(str.upper())

### Converting only first character of string to upper case

modified_str = str[0].upper() + str[1:]

# Print the modified string

print(modified_str)

### Checking if string is in lower case or upper case

print(str.isupper())
print(str.islower())

### Checking if string is digit, alpabetic, alpha-numeric

print(str.isdigit())
print(str.isalpha())
print(str.isalnum())

# assign "C++ is easy to learn" to a new_str variable

new_str = "C++ is easy to learn"
print(new_str)

### Replace C++ with Python

new_str = new_str.replace("C++", "Python")
print(new_str)

### Use Split function on new_str ###

new_str = new_str.split(" ")
new_str

# # **`Python Functions`**


"""
def function_name():
    stetement(s)
"""

# define a function with welcome_message(name) and body 'Welcome to Functions !!!'

def welcome_message(name):
    body = 'Welcome to Functions !!!'
    print(body)

# Example usage:

name = 'Shuvra'
welcome_message(name)

# call a function with your name

welcome_message

# * `def` Keyword marking start of function
# * `function name` to uniquely identify function
#     * `function naming` follows same `rules of writing identifiers`
# * `parameters`(arguments) to pass values to a function => totally optional
# * `()` paranthesis
# * `colon (:)` start of function
# * `documentation string`(docstring) describe's what function does => totally optional
# * `return statement` returns a value from function => totally optional
# * inside colon is `function definition` it should always be present before function call or get an error


# Write a function to add two number which are as 3 and 4
# in total variable store adition of 3 + 4
# print total variable

def add(x, y):
    z = x + y
    print(z)

add(3,4)

# # ***`Positional Arguments`***
# Most arguments are identified by their position in function call
# * Say `print(x,y)` will give different results from `print(y,x)`
#
# What ever sequence is given while defining a function values must be taken in that sequence only
# * Otherwise use argument name **`(keyword arguments)`** to take values
# * We first define `positional argument` and then `keyword arguments`
#


## Create subtraction_function(small_number,large_number) and return difference between large_number and small_number

def subtraction_function(small_number, large_number):
    difference = large_number - small_number
    return difference

# pass arguments in right order

small_number = 3
large_number = 10
result = subtraction_function(small_number, large_number)
print(f"The difference between {large_number} and {small_number} is {result}")

# always pass arguments using there name(keyword arguments) then order does not matter

result = 75 - 21
print("Result of 75 - 21 is:", result)



# # ***`Scope of Variables`*** means that part of program where we can access particular variable
# * `Local Variable` => variables defined inside a function and can be only accessed from inside of that particular function
# * `Global Variable` => variables defined outside a function and can be accessed throughout program
#
# Let's define a global variable, `"global_variable"` outside function
# * We will return its value using a function `"randome_function"` and see that we would be able to access its value using that function also


#### Observe every output from here onwords #####
# defining a global variable
global_variable = 'variable outside of function'

# defining function
def random_function():
    # accessing variable which is outside of this function
    return global_variable

random_function()

# `See we can acess the data of gobal variable from Inside of the Function`
#
# # **`=> Let's see what will happen if we try to change value of global variable from Inside of the Function`**


#### Observe every output from here onwords #####
# defining a global variable
global_variable = 'variable outside of function'

# defining function
def random_function():
    # changing value of global variable from inside of the function
    global_variable = 'changing variable outside of function from inside of function'
    # accessing variable which is outside of this function
    return global_variable

print(random_function())
print(global_variable)