class Circle():

    pi = 3.14

    def __init__(self, radius = 1):
        # Default radius is 1 if we dont provide parameter
        self.radius = radius

    def set_radius(self, new_r):
        self.radius = new_r


    def area(self):
        return self.radius * self.radius * Circle.pi

myc = Circle(3)

# updating attributes
myc.radius = 100
# updating attributes using method`
myc.set_radius(1000)

print(myc.area())