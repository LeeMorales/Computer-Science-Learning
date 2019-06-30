import time
from functools import wraps
from inspect import signature
def timethis(func):
    '''
    Decorator that reports the execution time.
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result
    return wrapper

@timethis
def countdown(n):
    """
    Counts down
    """
    while n > 0:
        n -= 1
countdown(100000)
countdown(10000000)

print(countdown.__name__)
print(countdown.__doc__)
print(countdown.__annotations__)
print(signature(countdown)) 
@timethis

def decorator1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Decorator 1')
        return func(*args, **kwargs)
    return wrapper


def decorator2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Decorator 2')
        return func(*args, **kwargs)
    return wrapper


@decorator1
@decorator2
def add(x, y):
    return x + y

add(1, 2)
print('-----------------')
print(add.__wrapped__(2, 3))