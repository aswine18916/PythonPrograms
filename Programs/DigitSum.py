"""Input two numbers r and s.
finding the numbers with r digigts whose sum is s
For ex: if r =3  and s=6, the program returns all 3 digit numbers whose sum is 6"""
import math
a=[]

r= int(input("Please enter a positive integer value for the number of digits : "))
s=int(input("Please enter positive integer fro the sum of digits : "))

if r == 1:
     print("The expected list is", str(s))
     print("The count of records with the condition is" ,str(r))
else:
    def getSum(n):
            sum = 0
            while (n != 0):
                sum = sum + int(n % 10)
                n = int(n/10)
            return sum

    def findcount():
                k=int((math.pow(10,r-1)))
                t= int((math.pow(10,r))-1)
                for i in range(k,t+1):
                    if getSum(i) == s:
                        a.append(i)
                    else:
                        continue
                print("The expected list is", str(a))
                print("The count of records satisfying the condition is" ,len(a))


    findcount()









      
           