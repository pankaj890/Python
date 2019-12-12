class Dog():

    # Class object attribute
    species = 'mammal'

    def __init__(self, breed, name):
        # Constructor - Special Method
        # This method refers to itself
        self.breed = breed
        self.name = name

    # Methods


mydog = Dog(breed = 'Lab', name = 'Sammy')

print(type(mydog))
print(mydog.breed)
print(mydog.name)
print(mydog.species)