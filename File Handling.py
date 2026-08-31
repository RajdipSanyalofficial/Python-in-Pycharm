# Read
a=open(r"C:\Users\HP\Downloads\files (1)\blinkit_products.csv")
b=a.read()
print(b)

# ------------------------------------------------------------------------------------------------------------
# read -> it reads the entire text in a file
# readline() -> It reads one line by line
# readlines() -> It reads list of strings
#
# To performing any operation in file handling first need to open the file
# by using open() function.
# open("file path",mode="")
# ------------------------------------------------------------------------------------------------------------


# ------------------------------------------------------------------------------------------------------------
# mode means in which file is opening r,w,a,x,rb/rw
# r -> reads the file only
# w -> writes file only if it is not present then at first it is created
# a -> appending the text at the end if the file is not present then it is created first
# x -> This mode is used to only create file but not for reading or writting texts inside the file.
# ------------------------------------------------------------------------------------------------------------

c=open("Hi.txt","w")
d=c.write("Hi I am Rajdip Sanyal !!!")
print(d)

d=open("Hi.txt","a")
e=d.write("\n This is appending text...............")
print(e)

# # How to handle different files
# # CSV
# PDF

# How to read csv file without pandas
import csv
s=open(r"C:\Users\HP\Downloads\archive (13)\zepto_v1.xlsx")
x=csv.reader(s) #csv.reader()

from PyPDF2 import PdfReader

s1 = open(r"C:\Users\HP\Downloads\vertopal.com_Numpy Practice 1 (1).pdf", "rb")
s2 = PdfReader(s1)
print(s2)

with open(r"Hi.txt") as f:
    a=f.read()
print(a)

import os
os.rename("Hi.txt","Hello.txt")
