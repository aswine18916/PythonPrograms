import re
sentence=" Hello  World   From Aswin   "
# print(sentence.strip())
# print(re.sub(" ", "", sentence))
spl=sentence.split()
print(spl)
print(" ".join(spl))