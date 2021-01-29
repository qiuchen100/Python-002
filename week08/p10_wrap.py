# -*- coding: utf-8 -*-

from functools import wraps


def route(func, text='abc'):
    @wraps(func)
    def decorator(a, b):
        print('Starting...')
        ret = func(a, b)
        print('ended...')
        return ret
    return decorator


@route(text='c')
def add(a, b):
    return a + b


t = add(3, 4)
print(t)
print(add.__name__)