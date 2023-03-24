arr_1=[1,2,4,5,6,7,9]
arr_2=[3,4,9,0,2,1,4,9]
total=6
final=arr_1+arr_2
count=0
# for i in arr_1:
#  for j in arr_2:
#   if i+j==total:
#    final.append(arr_1.index(i)+arr_2.index(j))
#    count=count+1
#    mymin = min([r for r in final])
#    print(mymin)
#    print (final)
#   else:
#    pass
# if count==0:
#  print([-1,-1])

filter= [final[i:i+3] for i in range(0, len(final),3)]
print(filter)