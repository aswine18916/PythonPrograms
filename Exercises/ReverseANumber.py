

def reverse(n):
    rev=0
    if n<0:
        print("enter a positive number")
    else:

        while (n>0):
            r=n%10
            rev=r+(rev*10)
            n=n//10
        print(rev)

reverse(-324)