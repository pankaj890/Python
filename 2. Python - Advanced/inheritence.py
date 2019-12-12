class Animal():
    def __init__(self):
        print('Animal Created')

    def whoAmI(self):
        print('Animal')

    def eat(self):
        print('Eating')


class Dog(Animal):     # Dog inherited Animal class
    def __init__(self):
        Animal.__init__(self)
        print('Dog Created')

    def bark(self):
        print('Woof')

    # Over-riding parent class method
    def eat(self):
        print('Dog Eating')


mydog = Dog()
mydog.whoAmI()
mydog.eat()
mydog.bark()