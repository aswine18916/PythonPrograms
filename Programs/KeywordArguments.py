"""Use of Keyworded arguments in a function"""
def introduction(**data):
    for k,v in data.items():
        print("{} is {}".format(k,v))

introduction(Firstname="Aswin", Lastname="Edavalath", Age=32, Phone=1234567890)