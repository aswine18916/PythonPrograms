new=[1,2,3,4,5,6,7,8,9,10,11]
k=3
res=[]
for i in range(0,len(new),k):
    res.extend(new[i:i+k])
print(res)