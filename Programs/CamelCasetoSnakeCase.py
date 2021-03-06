"""Converting a camel case Sentence to snake case Sentence"""
sentence="MyNameIsAswin"
newstring=""
final=""
for c in sentence[1:]:
    if c.isupper():
        c="_"+c
    newstring=newstring+c
final=sentence[0]+newstring
print(final)





