number=[0,5,0,0,3,1,15,0,12,0,0,0]
# listA=[i for i in number if i!=0]
# listB=[i for i in number if i==0]
# newlist=listA+listB
# print(listA)
# print(newlist)

while number[-1]==0:
    number.pop(-1)
print(number)
