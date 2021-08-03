class A:

    def __init__(self):
        print("in A Init")

    def feature1(self):
        print("Feature 1-A working")

    def feature2(self):
        print("Feature 2-A working")

class B:

    def __init__(self):
        # super().__init__()
        print("in B Init")

    def feature1(self):
        print("Feature 1-B working")

    def feature2(self):
        print("Feature 2-B working")

class C(A,B):

    def __init__(self):
        super().__init__()
        print("in C init")


    def feat(self):
        super().feature2()
        super().feature2()


a1 = C()
b1=B()
