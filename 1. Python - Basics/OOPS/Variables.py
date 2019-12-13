class Car:

    # Class variables
    # Common for all class objects
    wheels = 4


    def __init__(self):
        # Instance variables
        # stored in Instance Namespace
        self.mil = 10
        self.com = 'BMW'


c1 = Car()
c2 = Car()

print(c1.wheels)
print(c2.wheels)

Car.wheels = 6

print(c1.wheels)
print(c2.wheels)
