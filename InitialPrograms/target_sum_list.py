def twoSum(nums,target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] == target - nums[i]:
                return [i, j]

test=[3,3]
sum=6
print(twoSum(test,sum))