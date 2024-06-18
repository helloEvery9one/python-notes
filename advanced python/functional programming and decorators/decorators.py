'''decorators'''
from time import time
# decorators are functions that supercharge another function, giving it more functionality


def my_decorator(func):
    '''sdf'''
    def wrap_func(*args, **kwargs):
        print('*********')
        func(*args, **kwargs)
        print('*********')
    return wrap_func


# @my_decorator
# def hello():
#     '''sadf'''
#     print('hello')


# @my_decorator
# def bye():
#     '''s'''
#     print('see ya later!')
# hello()
# bye()

# ---------------------------------decorators part 2------------------------------------
@my_decorator
def hello(greeting):
    '''s'''
    print(greeting)


hello('wef')


def performance(func):
    '''sdf'''
    def wrapper(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'took {t2 - t1} seconds to run')
        return result
    return wrapper



@performance
def long_time():
    '''asdf'''
    for i in range(98000):
        print(i)


long_time()
