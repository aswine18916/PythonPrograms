def compute_number(s):
    def is_palindrome(s):
        if s == s[::-1]:
            return True
        return False
 #   f = False
    ctr = 0
    while len(s) > 0:
        if is_palindrome(s):
 #           f = True
            break
        else:
            ctr += 1
            s = s[0:len(s)-1]
    return ctr

print(compute_number('abcde'))