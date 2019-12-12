# Function modifies the functionality of another function
# Short down the code in a more pythonic 
# Used in Python web frameworks

s = 'Global Variable'


def func():
    global s        # will refer global variable
    s = 50
    print(s)


def func1():
    mylocal = 10
    print(locals())     # Prints local valriables as dictionary
    #print(globals())    # Prints global valriables as dictionary
    print(globals()['s'])


def hello(name = 'Pankaj'):
    return ('Hello' + name)


def hello1(name = 'Pankaj'):
    print('Hello() func has been run')
    def greet():
        return 'it is inside greet'
    def welcome():
        return 'It is inside welcome'
    print(greet())
    print(welcome())
    print('end of hello()')
    
def hello2(name = 'Pankaj'):
    print('Hello() func has been run')
    def greet():
        return 'it is inside greet'
    def welcome():
        return 'It is inside welcome'
    
    if name == 'Pankaj':
        return greet
    else:
        return welcome

# Function as a Argument
def hello3():
    return 'Hi Pankaj'

def other(func):
    print('hello')
    print(func())
    

#func()
#print(s)

#func1()

#print(hello())
#mynewgreet = hello         # Reassigning Func name
#print(mynewgreet())

#hello1()
#welcome()     # Error - due to scope of this funcrion
        
#x = hello2()
#print(x())

other(hello3)