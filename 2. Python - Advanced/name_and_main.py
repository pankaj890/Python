def func():
	print('this is func')

# __name__ is a variable which stores the module name
if __name__ == '__main__':
	print('It is called directly')
	print(__name__)
else:
	print('It is called indirectly/imported')
