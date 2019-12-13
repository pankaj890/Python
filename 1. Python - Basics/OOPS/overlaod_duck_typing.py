class Pycharm:

    def execute(self):
        print('compiling')
        print('running')


class MyEditor:

    def execute(self):
        print('Spell Checking')
        print('Naming Convention Checking')
        print('compiling')
        print('running')


# Here we have the same method name and we are not concern about its class
# execute() method is in Pycharm and MyEditor
class Laptop:

    def code(self, ide):
        ide.execute()


ide = Pycharm()

lap1 = Laptop()
lap1.code(ide)
