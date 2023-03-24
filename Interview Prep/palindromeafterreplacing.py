def isPossiblePalindrome(str):
    n = len(str)
    for i in range(n // 2):

        if (str[i] != '.' and
                str[n - i - 1] != '.' and
                str[i] != str[n - i - 1]):
            return False

    return True



def smallestPalindrome(str):
    if (not isPossiblePalindrome(str)):
        return "Not Possible"

    n = len(str)
    str = list(str)


    for i in range(n):
        if (str[i] == '.'):

            if (str[n - i - 1] != '.'):
                str[i] = str[n - i - 1]


            else:
                str[i] = str[n - i - 1] = 'a'

    # return the result
    return str

print(smallestPalindrome("fdfd."))