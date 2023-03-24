inp="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
def longestPalindrome(s):
    if len(str(set(inp)))==1:
        return inp
    else:
        max=0
        res=0
        final=""
        current=""
        for i in range(len(s)):
            for each in s[i::]:
                final=final+each
                if final==final[::-1]:
                    res=len(final)
                    if res > max:
                        max = res
                        current = final
                    else:
                        max = max
                else:
                    continue

            final=""
        return current


print(longestPalindrome(inp))