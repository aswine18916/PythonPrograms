"""
From sentence print a list with only one copy of each word from the previous
"""
import re
x=[]
s="Hello Hello, My Name Name is is is Aswin. I am an engineer by profession"
new=re.sub('[,.]',"",s)

final=new.split()
for each in final:
    if each not in x:
        x.append(each)

print(x)
print(' '.join(x))

