number=[1,2,4,5,6,7,9]
square=47
i=0
success=False
while i < len(number):
    if number[i]**2 > square:
        print(number[i], "square is greater than",square)
        success=True
    if not success:
        print(number[i], "square is not greater than",square)
    i=i+1