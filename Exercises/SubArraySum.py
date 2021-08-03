import sys


# def kadane(A):
#     # stores the maximum sum sublist found so far
#     max_so_far = 0
#
#     # stores the maximum sum of sublist ending at the current position
#     max_ending_here = 0
#
#     # traverse the given list
#     for i in A:
#         # update the maximum sum of sublist "ending" at index `i` (by adding the
#         # current element to maximum sum ending at previous index `i-1`)
#         max_ending_here = max_ending_here + i
#
#         # if the maximum sum is negative, set it to 0 (which represents
#         # an empty sublist)
#         max_ending_here = max(max_ending_here, 0)
#
#         # update the result if the current sublist sum is found to be greater
#         max_so_far = max(max_so_far, max_ending_here)
#
#     return max_so_far
#
#
# A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# for kadane in sys.stdin:
#    print(type(kadane),end="")

    
for line in sys.stdin:
    if 'Exit' == line.rstrip():
        break
    print(f'Processing Message from sys.stdin *****{line}*****')
print("Done")
