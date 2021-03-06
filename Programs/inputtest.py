import re
newlist=[]
file= open("input.txt", 'r')
k=file.read()
print(k)

for line in file:
    for word in line.split():
       newlist.append(word)
print(newlist)
c=0
freq={}
for char in newlist:
    if char in freq:
        freq[char]+=1
    else:
        freq[char]=1
print(freq)







