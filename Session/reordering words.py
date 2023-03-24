inputword=" My Name is Aswin I am an Engineer by Profession"

def reorder_word(inputword):
    inputword=inputword[::-1]
    final=""
    words=inputword.split(" ")
    for word in words:
        word=word[::-1]
        final=final+ " " + word
    return final


print(reorder_word(inputword))