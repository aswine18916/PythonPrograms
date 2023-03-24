arr=[37, 32, 97, 37, 37, 32, 62, 35, 76, 62]
new=list(set(arr))

count=(len(arr)-len(new))

print(count)



# def equalizeArray(arr):
#     # Write your code here
#     new = list(set(arr))
#     final = []
#     if len(arr) == len(new):
#         return len(arr) - 1
#     else:
#         for each in new:
#             if arr.count(each) > 1:
#                 final.append(arr.count(each))
#         return len(arr) - max(final)
#
#
# result=equalizeArray(arr)
# print(result)