"""Converting a camel case sentence to snake case sentence"""
sentence="MyNameIsAswin"
newstring=""
final=""
for c in sentence[1:]:
    if c.isupper():
        c="_"+c
    newstring=newstring+c
final=sentence[0]+newstring
print(final)





