A=[1,2,3,4,5,1,2,3,4,2,3,4,5,6,7,8,5,3,6,8]

refine=list(set(A))

print(refine)
for each in refine:
    print("Count of {} in A is {}".format(each, A.count(each)))
