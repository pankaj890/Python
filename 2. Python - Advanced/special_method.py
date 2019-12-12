# Special Methods
    # to perform special tasks
    # can be called only by specific python syntax

class Book():

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # String representation of an Object
    # When we print the object, this method will execute
    def __str__(self):
        return "Title:{},Author:{},Pages:{}".format(self.title,self.author,self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book is destroyed")

# Object Creation
b = Book('Python', 'Pankaj', 100)

# print(b)          __str__()
# print(len(b))     __len__()
del b               __del__()