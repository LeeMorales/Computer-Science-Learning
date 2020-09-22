from functools import wraps, partial
import logging
import time


def logged(level, name=None, message=None):
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)

        return wrapper

    return decorate
    @logged(logging.DEBUG)
    def add(x, y):
        return x + y
    @logged(logging.CRITICAL, 'example')
    def spam():
        print('Spam!')
    def attach_wrapper(obj, func=None):
        if func is None:
            return partial(attach_wrapper, obj)
        setattr(obj, func.__name__, func)
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__
        @wraps(func)

        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)
        @attach_wrapper(wrapper)
        def set_level(newlevel):
            nonlocal level
            level = newlevel
        @attach_wrapper(wrapper)
        def set_message(newmsg):
            nonlocal logmsg
            logmsg = newmsg
            return wrapper
            return decorate
        @logged(logging.DEBUG)
        def add(x, y):
            return x + y
            @logged(logging.CRITICAL, 'example')
            def spam():
                print('Spam!')
                logging.basicConfig(level=logging.DEBUG)
                add(2, 3)
                add.set_message('Add called')
                add(2, 3)
                add.set_level(logging.WARNING)
                add(2, 3)

                print('---------------------')
                spam()
                spam.set_message('Add called')
                spam()
                spam.set_level(logging.WARNING)
                spam()