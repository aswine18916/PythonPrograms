n=19


def isHappy(n):
    c = 10
    while c:
        n = str(n)
        l = [int(i) ** 2 for i in n]
        if sum(l) == 1:
            return True
        else:
            n = sum(l)
        c -= 1
    return False

print(isHappy(19))

