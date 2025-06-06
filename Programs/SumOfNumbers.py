
"""User inputs three number and find the sum of all digits between these numbers in the format given
i,j,k are three numbers
sum=i+(i-1)+(i-2)+(i-3)+...+j+(j-1)+(j-2)+(j-3)+...k
ex: 10,8,15
This Program finds the sum in the format 15+14+13+12+11+10+9+8+9+10"""



def calculate_custom_sum(i, j, k):
    descending_part = list(range(i, j - 1, -1))
    ascending_part = list(range(j + 1, k + 1))
    total_sequence = descending_part + ascending_part
    total_sum = sum(total_sequence)
    expression = '+'.join(str(num) for num in total_sequence)
    print(expression)
    print("Sum:", total_sum)


# Example
i = 10
j = 7
k = 16
calculate_custom_sum(i, j, k)
