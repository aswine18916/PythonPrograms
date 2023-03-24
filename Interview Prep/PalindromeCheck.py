# def ispalindrome(word):
#     for i in range(int(len(word)/2)):
#         if word[i]==word[len(word)-i-1]:
#             pass
#         else:
#             print("not a palindrom")
#             break
#         print("is a palindrome")
#
# str="malayalam"
# ispalindrome(str)



def reverse(word):
    half1=""
    half2=""
    for i in range(int(len(word)/2)):
        half1=half1+word[len(word)-i-1]
        half2=half2+word[int((len(word)/2))-i-1]
    final=half1+half2
    print(final[::-1])


sentence="malayalam"

reverse(sentence)

