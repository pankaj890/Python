def fibon(n):
    a = b = 1
    for i in range(n):
        yield a            # Generator
        a, b = b, a+b


#for x in fibon(100):
#    print(x)



# MAP
items = [1, 2, 3, 4, 5]
print(list(map(lambda x:x**2, items)))

# FILTER
print(list(filter(lambda x: x < 0, range(-5,5))))

# REDUCE
from functools import reduce
print(reduce((lambda x,y: x*y), (items)))       # Factorial
