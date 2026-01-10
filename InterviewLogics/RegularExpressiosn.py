import re

str1="Hello123Howare456"
'''
print(re.match(r"[A-Za-z]",str1))

print(re.search(r"[0-9]",str1))

total=re.findall(r"\d+","Hello123Howare456")
print(total)
print(sum(map(int,total)))
'''
result=re.search("1",str1)