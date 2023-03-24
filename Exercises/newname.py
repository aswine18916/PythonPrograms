# import factorial
# print(factorial.__name__)


def even_number(start, n):
     final=([x for x in range(start,((2*n)+2)) if x%2==0 ])
     print(final)
     new=",".join(str(each) for each in final)
     print(new)
even_number(3,6)