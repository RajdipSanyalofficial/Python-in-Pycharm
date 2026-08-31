# Python Data Structure Assignment
# --------------------------------
# List
# ----

a=[]
print(type(a))

languages=["R","Python","SAAS","Java","Scala",42]
b=len(languages)
print(b) #6

for lan in languages:
    print(lan)

temp=languages[1]

print(temp)
print(type(temp))

c=languages.append("C Programming")
print(languages)
c1=languages.remove(42)
print(languages)



