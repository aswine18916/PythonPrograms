sentence="malayalam"
new=[]
count=0
for each in sentence:
    if each not in new:
        new.append(each)
for item in new:
    if sentence.count(item)>1:
        count=count+1
print(count)