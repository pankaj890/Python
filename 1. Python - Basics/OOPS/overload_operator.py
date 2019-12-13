###########################################################################
a = '10'
b = '20'
print(a+b)

# behind the scene, it works like below
# print(int.__add__(a,b))    # for Integer type
print(str.__add__(a, b))    # for String type

# + __add__()
# - __sub__()
# * __mul__()
#
###########################################################################


class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    # Magic Methods - Overload add (+) operator method
    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2

        stu_sum = Student(m1, m2)

        return stu_sum

    # Magic Methods - Overload Greater Than (>) operator method
    def __gt__(self, other):
        m1 = self.m1 + self.m2
        m2 = other.m1 + other.m2

        if m1 > m2:
            return True
        else:
            return False

    # Magic Methods - Overload String to print Class Object
    def __str__(self):
        # to return a string
        return '{} {}'.format(self.m1, self.m2)


s1 = Student(40, 80)
s2 = Student(50, 60)

# Add Operator
s3 = s1.__add__(s2)
print("Sum 1",  s3.m1)
print("Sum 2",  s3.m2)


# Greater Than Operator
if s1 > s2:
    print('\ns1 wins')
else:
    print('s2 wins')


# String Operator - below prints the same thing
print(s3)
print(s3.__str__())
