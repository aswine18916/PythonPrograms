s=[1,1,2]

def solution(nums):
    new=[]
    for each in nums:
        if each not in new:
            new.append(each)
    return new


print(solution(s))