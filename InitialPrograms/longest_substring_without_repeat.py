import re
sentence="babad"

def solution(s):
    new=""
    final=""
    current=""
    res=0
    max=0
    for each in s:
        if each not in new:
            new=new+each

    if len(new)==1:
        return 1
    elif len(new)==len(s):
        return len(new)
    else:
        for i in range(len(s)):
            for ele in s[i::]:
                if ele in final:
                    break
                else:
                    final=final+ele
                res=len(final)
                if res>max:
                    max=res
                    current=final
                else:
                    max=max
            final=""
    return current



print(solution(sentence))

