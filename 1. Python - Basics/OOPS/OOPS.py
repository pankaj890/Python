class Computer:

    # Constructor
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print('Config is :', self.cpu, self.ram)


com1 = Computer('i5', 16)
com2 = Computer('Ryzen 3', 8)

#print(type(com1))

# Ways to execute methods in a class
#Computer.config(com1)
com1.config()
com2.config()
