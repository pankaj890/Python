def new_decorator(func):
    def wrap_func():
        print('Code here before executing func')
        func()
        print('func has been called')
        
    return wrap_func


@new_decorator
def func_needs_decorator():
    print('This func is in need of a decorator')
    
# @new_deorator is equivalent to below line
#func_needs_decorator = new_decorator(func_needs_decorator)

func_needs_decorator()