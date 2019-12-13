class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    # No overloading in Python by default but we can achieve is this way
    @staticmethod
    def sum(a=None, b=None, c=None):
        if a != None and b != None and c != None:
            s = a + b + c
        elif a != None and b != None:
            s = a + b
        else:
            s = a
        return s


s1 = Student(40, 80)
print(s1.sum(5))
print(s1.sum(5, 5))
print(s1.sum(5, 5, 5))

