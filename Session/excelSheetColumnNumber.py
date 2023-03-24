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


print(titleToNumber(" "))