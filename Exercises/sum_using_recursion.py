def sum(n):
    if n==1:
        return 1
    else:
        s=0
        for i in range(n+1):
            s=sum(n-1)+i
        return s


print(sum(10))