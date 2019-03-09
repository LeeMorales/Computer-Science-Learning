def apply_async(func, args, *, callback):
    # Compute the result
    result = func(*args)

    # Invoke the callback with the result
    callback(result)
    from queue import Queue
from functools import wraps

class Async:
    def __init__(self, func, args):
        self.func = func
        self.args = args


    def inlined_async(func):
        def Queue():
            @wraps(func)
            def wrapper(*args):
                f = func(*args)
                result_queue = Queue()
                result_queue.put(None)
                while True:
                    print('1' * 15)
                    result = result_queue.get()
                    print('2' * 15)
                    try:
                        print('3' * 15)
                        print('result={}'.format(result))
                        a = f.send(result)
                        print('4' * 15)
                        apply_async(a.func, a.args, callback=result_queue.put)
                        print('5' * 15)
                    except StopIteration:
                        break

            return wrapper
            def add(x, y):
                return x + y  
@inlined_async
def test():
    print('start'.center(20, '='))
    r = yield Async(add, (2, 3))
    print('last={}'.format(r))
    r = yield Async(add, ('hello', 'world'))
    print('last={}'.format(r))
    # for n in range(10):
    # r = yield Async(add, (n, n))
    # print(r)
    # print('Goodbye')
    print('end'.center(20, '='))


if __name__ == '__main__':
    test()
    def sample():
        n = 0
    # Closure function
    def func():
        print('n=', n)

    # Accessor methods for n
    def get_n():
        return n

    def set_n(value):
        nonlocal n
        n = value

    # Attach as function attributes
    func.get_n = get_n
    func.set_n = set_n
    return func

f = sample()
f()
f.set_n(10)
f()

import sys
class ClosureInstance:
    def __init__(self, locals=None):
        if locals is None:
            locals = sys._getframe(1).f_locals

        # Update instance dictionary with callables
        self.__dict__.update((key,value) for key, value in locals.items()
                            if callable(value) )
    # Redirect special methods
    def __len__(self):
        return self.__dict__['__len__']()

# Example use
def Stack():
    items = []
    def push(item):
        items.append(item)

    def pop():
        return items.pop()

    def __len__():
        return len(items)

    return ClosureInstance()

s = Stack()
print(s)
s.push(10)
s.push(20)
print(len(s))
print(s.pop())
print(s.pop())