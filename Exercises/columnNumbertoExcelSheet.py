abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

number=986
ans=""
while number:
    ans=ans+abc[(number-1)%26]
    number=(number-1)//26
print(ans[::-1])
