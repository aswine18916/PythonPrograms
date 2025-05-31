def titleToNumber(columnTitle):
    if not columnTitle.isalpha():
        return None

    ans = 0
    for char in columnTitle:
        ans = ans * 26 + (ord(char.upper()) - ord('A') + 1)
    return ans


print(titleToNumber("ZZ"))     # 702



def let_to_num(char):
    abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    abc=abc.lower()
    return abc.index(char.lower()) + 1


def titleToNumber(columnTitle):
    if columnTitle.isalpha():
        ans = 0
        for i in range(len(columnTitle)):
            ans *= 26
            ans += let_to_num(columnTitle[i])
        return ans
    else:
        return None


print(titleToNumber("ZZ"))
