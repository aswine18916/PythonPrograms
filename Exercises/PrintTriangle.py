func_list=[]
def design(n):
    for i in range(n):
        for i in range(n):
            print("+", end="")
            for i in range(1, n):
                print("-", end="")
            print("+")
            print("|", end="")
            print((" " * 1) + str(5))
        print(end=" ")
    print(end=" ")
# def size(k):
#     for each in k:
#         c=c+1
#     return c

design(4)
# design()
# design()
