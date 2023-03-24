sentence="Hello World   "

def lengthOfLastWord(s):
    z = s.split()
    return (len(z[len(z) - 1]))


print(lengthOfLastWord(sentence))