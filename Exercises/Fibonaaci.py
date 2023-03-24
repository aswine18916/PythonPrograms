"""Fibonacci series using while loop"""
import operator
from functools import reduce

n=int(input("Enter the number: "))
new=[]
c=0
n1=1
n2=2
while c<n:
    print(n1)
    n3=n1+n2
    n1=n2
    n2=n3
    c=c+1
    new.append(n1)
print(new)
print(reduce(operator.add,new))


