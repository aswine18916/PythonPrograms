"""Input two numbers r and s.
Finding the numbers with r digits whose sum is s
For ex: if r =3  and s=6, the program returns all 3 digit numbers whose sum is 6"""
import math

a = []


def getSum(n):
    sum = 0
    while (n != 0):
        sum = sum + int(n % 10)
        n = int(n / 10)
    return sum


def findcount(r,s):
    k = int((math.pow(10, r - 1)))
    t = int((math.pow(10, r)) - 1)
    for i in range(k, t + 1):
        if getSum(i) == s:
            a.append(i)
        else:
            continue
    print("The expected list is", str(a))
    print("The count of records satisfying the condition is", len(a))


def checknum(r,s):
    if r == 1:
        print("The expected list is", s)
        print(type(s))
        print("The count of records with the condition is", r)
        print(type(r))
    else:
        findcount(r,s)



def checkint():
    x=1
    while x<10:
        r = input("Please enter a positive integer value for the number of digits : ")
        s = input("Please enter positive integer for the sum of digits : ")

        if r.isnumeric():

            if s.isnumeric():
                r=int(r)
                s=int(s)
                checknum(r,s)
            else:
                print("That's not right, start from begining")
                break
            break
        else:
            if x==8:
                print("Next is your last chance")
            if x==9:
                print("That's it.. Whatever you entered is not a positive digit, quitting the program")
            x=x+1



checkint()

