import re
sentence="Ab3"

c = 0
def minimumNumber(n, password):
    answer=0

    def checkvalue(password):
        global c

        if re.search("[a-z]", password):
            pass
        else:
            c = c + 1
        if re.search("[A-Z]", password):
            pass
        else:
            c = c + 1
        if re.search("[0-9]", password):
            pass
        else:
            c = c + 1
        if re.search("[!@#$%^&*()-+]", password):
            pass
        else:
            c = c + 1
        return c
    if n<6:
        if checkvalue(password)>(6-n):
            answer==checkvalue(password)
        elif checkvalue(password)>(6-n):
            answer=6-n
    elif n>=6:
        answer==checkvalue(password)

    print(answer)

minimumNumber(3,sentence)



# import re
#
# txt = "The rain in Spain"
# x = re.search("The", txt)
# print(type(x))