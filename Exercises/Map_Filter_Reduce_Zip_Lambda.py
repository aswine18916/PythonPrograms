from functools import reduce

print("-------------ZIP------------")
name = ["Manjeet", "Nikhil", "Shambhavi"]
marks = [40, 50, 60]

mapped = zip(name, marks)

print(dict(mapped))


print("------------REDUCE-----------")

seq=[1,2,3,4,5,6]
multiply=reduce(lambda a,b:a+b,seq)
print(multiply)


print("------------FILTER-----------")
seq = [0, 1, 2, 3, 4, 5]

# result contains odd numbers of the list
result = filter(lambda x: x % 2, seq)
print(list(result))

# result contains even numbers of the list
result = filter(lambda x: x % 2 == 0, seq)
print(list(result))


print("--------------MAP--------------")
nums = [1, 2, 3, 4, 5]
square = list(map(lambda x: x**x, nums))
print(square)

nums = [1, 2, 3, 4, 5]
def sq(n):
    return n*n
square = list(map(sq, nums))
print(square)