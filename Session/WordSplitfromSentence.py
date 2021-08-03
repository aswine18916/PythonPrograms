
"""
Splitting words from a sentence and capitilising each word
"""
sentence="catcollegecountrycrowncroatia"
for c in sentence:
    if c=='c':
        c=c.upper()
        c=" " + c
    print(c, end="")
