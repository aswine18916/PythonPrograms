nums= [-2,1,-3,4,-1,2,1,-5,4]
oneint=[1]

def solution(nums):
    current_max=nums[0]
    max_till_now=nums[0]

    for i in range(1,len(nums)):
        current_max=max(nums[i],current_max+nums[i])
        max_till_now=max(max_till_now,current_max)
    return max_till_now
print(solution(oneint))