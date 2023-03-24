
c=8
a = []
b = (1, 2)
test = {}


def aux0(d):
    global c
    a.append(d)


def aux2(c):
    c = 3


def aux3(i):
    b = (3, 2)
    test['5'] = 7


def aux4(i):
    b[0] = 5


for f in [aux0, aux2, aux3, aux4]:
    try:
        print(f.__name__)

        f(5)

        print("c", c)
        print("a", a)
        print("b", b)
        print("test", test, end="\n")
        print("-------------------------")



    except Exception as e:
        print
        "Error: %s" % e

