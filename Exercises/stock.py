

import itertools
import operator

currentValue=[175, 133, 109, 210, 97]
futureValue=[200, 125, 128, 228, 133]

saving=250
def optimised_stock_solution(saving,cv,fv):
    n = len(cv)
    fr = [[x for x in range(n+1)] for y in range(saving+1)]
    for i in range(1, saving+1):
        for j in range(1, n+1):
            if cv[j-1]<=i:
                fr[i][j]=max(fr[i][j-1],fr[i-cv[j-1]][j-1]+fv[j-1]-cv[j-1])
            else:
                fr[i][j]=fr[i][j-1]


    print(fr[saving][n])

optimised_stock_solution(saving,currentValue,futureValue)