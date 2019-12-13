class Student:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.rollno)

    class Laptop:
        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 8

        def show(self):
            print(self.brand)
            print(self.cpu)
            print(self.ram)


s1 = Student('Navin', 2)
s2 = Student('Jenny', 3)

s1.show()

lap1 = s1.lap
lap2 = s2.lap
print(id(lap1))
print(id(lap2))

# creating inner class object and call inner class method
lap1 = Student.Laptop()
lap1.show()
