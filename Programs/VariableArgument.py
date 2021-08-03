"""Program 1"""
def add(*num):
    sum = 0
    for n in num:
        sum = sum + n
    print(sum)


add(3, 5, 6)
add(6,7,8,9,1)


"""Program 2"""
def mult_table(*n):
    for k in n:
        print(k, "*", 5, "=", k*5)

mult_table(4,5,6)