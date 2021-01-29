# -*- coding: utf-8 -*-

class Counter(object):


    def __init__(self, fun, cnt=0):
        self._func = fun
        self._cnt = cnt

    def __call__(self, *args, **kwargs):
        self._cnt += 1
        print(f'num of function {self._func.__name__} called : {self._cnt}')
        return self._func(*args, **kwargs)


@Counter
def func(a, b):
    c = a + b
    print(f'{a} + {b} = {c}')


@Counter
def func2(a, b):
    c = a - b
    print(f'{a} - {b} = {c}')


if __name__ == '__main__':
    func(3, 4)
    func2(3, 4)
    func(2, 4)
    func2(2, 4)
    func(90, 4)
    func2(90, 4)

