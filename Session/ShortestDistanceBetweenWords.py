inputlist = ["My", "Name", "is", "Aswin", "Name", "QA", "Engineer", "is", "My"]


def ShortDistance(word1, word2):
    x = inputlist.index(word1)
    y = inputlist.index(word2, 0, x)
    z = inputlist.index(word2, x)
    print(x, y, z)
    print(x - y)
    print(z - x)
    if (x - y) > (z - x):
        print("shortest distance is", z - x)
    elif (z - x) > (x - y):
        print("shortest distance is", x - y)


ShortDistance("Aswin", "is")
