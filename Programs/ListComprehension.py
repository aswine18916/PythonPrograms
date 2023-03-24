# """List comprehension examples"""
# """Program 1"""
# # man=[c for c in 'human']
# # print(man)
#
# """Program 2"""
#
# even=[x for x in range(50) if x%2==0 and x%5==0]
# print(even)
#
# """Program 3"""


scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]

# def is_A_student(score):
#     return score > 75

over_75 = tuple(filter(lambda score: score>75, scores))

print(over_75)




