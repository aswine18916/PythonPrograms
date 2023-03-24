class A:
    def who_am_i(self):
        print("I am a A")

class B(A):
    def who_am_i(self):
        print("I am a B")
        super().who_am_i()
    pass

class C():
    def who_am_i(self):
        print("I am a C")
    pass

class D(B,C):
    def who_am_i(self):
        # print("I am a D")
        super().who_am_i()
    pass

d1 = D()
d1.who_am_i()

# b1=B()
# b1.who_am_i()
