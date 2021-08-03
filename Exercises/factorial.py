"""Factorial of a number using recursion"""

t=int(input("Enter the number of input : "))

def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x - 1))



print("Factorial is :", factorial(t))
