class Student:

    school = 'Telusko'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    # Instance Method - Uses class objects
    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3

    # Accessor method of Instance Methods
    def get_m1(self):
        return self.m1

    # Mutator method of Instance Methods
    def set_m1(self, value):
        self.m1 = value

    # Class method
    @classmethod
    def get_School(cls):
        return cls.school

    # Static Method
    @staticmethod
    def info():
        print('This Student class')

s1 = Student(34, 67, 32)
s2 = Student(89, 32, 12)
s3 = Student(40, 50, 60)

print(s1.avg())
print(s2.avg())
print(s3.avg())

print(s1.get_School())
Student.info()

