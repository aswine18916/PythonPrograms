nums=[4,1,2,1,2]
final=[each for each in nums if nums.count(each)==1]
# print(final)
print(''.join([str(x) for x in final]))