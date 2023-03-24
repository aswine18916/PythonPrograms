n=121
rev=0
while(n!=0):
    r=int(n%10)
    rev=rev*10+r
    n=n//10
print(rev)  