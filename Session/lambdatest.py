newtest= lambda  n: n+10

print(newtest(20))

def calculateSquare(n):
    return n*n


numbers = (1, 2, 3, 4)
result = map(calculateSquare, numbers)
setresult=set(result)
print(setresult)