
"""User inputs three number and find the sum of all digits between these numbers in the format given
i,j,k are three numbers
sum=i+(i-1)+(i-2)+(i-3)+...+j+(j-1)+(j-2)+(j-3)+...k
ex: 10,8,15
This Program finds the sum in the format 15+14+13+12+11+10+9+8+9+10"""
def sum_of_numbers(i,j,k):

    if i==j and i==k:
        long=i+j+k
    else:
        list=[]
        list.append(i)
        list.append(j)
        list.append(k)
#        print(list)

        l=max(list)
#        print(l)
        s=min(list)
#        print(s)
        for x  in list:
            if x!=l and x!=s:
                m=i

#    print(l,m,s)
        y=sum(range(s,l))
        z=sum(range(m,l))
        long=y+z+l
        print(z)
        print(y)
    print(long)

sum_of_numbers(5,8,11)