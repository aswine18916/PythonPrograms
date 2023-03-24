A=[3,3,3,2,6,7]
# [3,3,3,5,4,1]
n=len(A)
k=int(n/2)
if n==1:
    print("Single element list")
if n>=2:
    if n%2!=0:
        print("List should be even in number")
    else:
        if sum(A[0:k])==sum(A[k:n]):
            print("Its a match")
        else:
            print("It's not a match")

