def climbStairs(n):
    if n <= 2:
        return n
    steptwo = 1
    stepone = 2
    result = 0

    for i in range(2, n):
        result = steptwo + stepone
        steptwo = stepone
        stepone = result
    return result


print(climbStairs(5))