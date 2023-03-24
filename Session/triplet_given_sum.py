A=[4,7,6,12,9,1,11,8]
sum=13
for i in range(0,len(A)-2):
    for j in range(i+1,len(A)-1):
        for k in range(j+1,len(A)):
            if A[i]+A[j]+A[k]==sum:
                print(A[i], A[j], A[k])
            else:
                continue
