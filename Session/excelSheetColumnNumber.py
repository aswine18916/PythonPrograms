def titleToNumber(columnTitle):
    if not columnTitle.isalpha():
        return None

    ans = 0
    for char in columnTitle:
        ans = ans * 26 + (ord(char.upper()) - ord('A') + 1)
    return ans

# Test case
print(titleToNumber(" "))      # Returns None
print(titleToNumber("A"))      # 1
print(titleToNumber("Z"))      # 26
print(titleToNumber("AA"))     # 27
print(titleToNumber("ZZ"))     # 702
print(titleToNumber("AAA"))    # 703
