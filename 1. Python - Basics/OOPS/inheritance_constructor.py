class A:

    # Super constructor
    def __init__(self):
        print('In A init')

    def feature1(self):
        print('feature 1 running')

    def feature2(self):
        print('feature 2 running')


class B(A):

    # Child constructor
    def __init__(self):
        super().__init__()
        print('In B init')

    def feature3(self):
        print('feature 3 running')

    def feature4(self):
        print('feature 4 running')


class C:

    # Child constructor
    def __init__(self):
        print('In C init')

# Constructor in Multiple Inheritance where we have multiple super constructors
# Method Resolution Order
class D(A, C):

    def __init__(self):
        super().__init__()
        print('In D init')


a1 = D()
