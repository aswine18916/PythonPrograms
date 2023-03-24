from turtle import width

x=int(input("Number of rows : "))
y= int(input("Number of columns : "))
k=int(x/2)
for i in range(0,k):
    pattern="A" * ((2*i)+1)
    print(pattern.center(y,'-'))
print("A".center(y,'-'))