def sub_array_with_sum(l):
    if len(l)==0:
        return None
    sum_l=sum(l)
    if sum_l%2==1:
        return None
    target_sum=sum_l/2
    running_sum=-0
    for i in range(len(l)):
        running_sum=running_sum+l[i]
        if running_sum==target_sum:
            return l[:i+1],l[i+1:]
    return None


print(sub_array_with_sum([1,2,4,6,1]))