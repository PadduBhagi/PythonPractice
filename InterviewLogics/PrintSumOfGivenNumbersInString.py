
'''
str1="S11R221"
sum=0
alpha=""
for char in str1:
    if char==['a-z','A_Z']:
        alpha=alpha+char
        print (alpha)
    elif char==[0-9]:
        sum=sum+int(char)
        print(sum)

str1 = "S11R221"
total = 0
alpha = ""

for char in str1:
    if char.isalpha():
        alpha = alpha + char
    elif char.isdigit():
        total = total + int(char)

print("Alphabets:", alpha)
print("Sum:", total)
'''
import re

str1 = "S11R221@g13il.com"
total = 0
alpha = ""

for char in str1:
    if re.match(r"[A-Za-z]", char):
        alpha = alpha + char
    elif re.findall(r"\d", char):
        total = total + int(char)

print("Alphabets:", alpha)
print("Sum:", total)