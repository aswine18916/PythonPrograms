inputword=" My Name is Aswin"
inputword=inputword[::-1]
final=""
words=inputword.split(" ")
for word in words:
    word=word[::-1]
    final=final+ " " + word
print(final)