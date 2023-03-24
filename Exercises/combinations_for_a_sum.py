import itertools

lis=[3,7,1,2,8,4,5]
target=21
n=3
c=0
final=list(itertools.combinations(lis,n))
for each in final:
    each=list(each)
    if sum(each)==target:
        c=c+1
if c>1:
    print("the total combinations are {}".format(c))
else:
    print("no combination")