A=[1,2,5,9,9]
X=5
def solution(A, X):
    N = len(A)
    if N == 0:
        return -1
    l = 0
    r = N - 1
    while l < r:
        m = (l + r) // 2
        if A[m] > X:
            r = m - 1
        else:
            l = l+1
    if A[l] == X:
        return l
    return -1

print(solution(A,X))