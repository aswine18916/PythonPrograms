
"""Finding the number of each word in a sentence"""

str= "Hello Hello How are are are you you you"
low=str.lower()
low=low.split(" ")

word=[]
for i in low:
    if i not in word:
        word.append(i)
print(word)
for i in range(0,len(word)):
    print("count of", word[i], "is :", low.count(word[i]))

