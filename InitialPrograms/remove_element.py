nums=[0,1,2,2,3,0,4,2]
val=2
new=[]
for each in nums:
    if each==val:
        continue
    else:
        new.append(each)
print(len(new))