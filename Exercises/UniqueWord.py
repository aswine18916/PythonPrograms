"""
From sentence print a list with only one copy of each word from the previous
"""
import re
s="Hello Hello, My Name Name is is is Aswin. I am an engineer by profession"
s=re.sub("[,./]", '', s)
s=re.sub("/", ' ', s)
s=s.split(" ")
#print(s)
#print(len(s))
unique=[]
for word in s:
    if s.count(word)==1:
        unique.append(word)
    if s.count(word)>1:
        if word not in unique:
            unique.append(word)
print(unique)




