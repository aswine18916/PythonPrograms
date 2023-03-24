import re
s="{()}}}"
def isValid(s):
    stack = []
    dictt = {"(": ")", "{": "}", "[": "]"}
    for i in s:
        if i in dictt:
            stack.append(i)
        elif stack == [] or dictt[stack.pop()] != i:
            return False
    return stack == []

print(isValid(s))