class A:

    def feature1(self):
        print('feature 1 running')

    def feature2(self):
        print('feature 2 running')


# Single Inheritance
class B(A):

    def feature3(self):
        print('feature 3 running')

    def feature4(self):
        print('feature 4 running')


class C:
    def feature5(self):
        print('feature 5 running')


# Multi-Level Inheritance --- D inherits B inherits A
class D(B):
    def feature6(self):
        print('feature 6 running')


# Multiple Inheritance --- E inherits A and C
class E(A, C):
    def feature6(self):
        print('feature 6 running')
