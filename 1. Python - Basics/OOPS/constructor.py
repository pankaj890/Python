class Computer:
    def __init__(self):
        self.name = 'Pankaj'
        self.age = 28

    def update(self):
        self.age = 40

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False


c1 = Computer()
c2 = Computer()


# Address in the memory
# Different for different objects
print(id(c1))
print(id(c2))

c1.update()
print(c1.age)
print(c2.age)

# Size of object depends on Constructor

# Comparison between objects by values
if c1.compare(c2):
    print('Same')
else:
    print('Different')