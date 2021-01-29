# -*- coding: utf-8 -*-
from functools import wraps


def autograph(**kwds):
    # wraps(f)

    def decorator(f):
        for k in kwds:
            if not hasattr(f, k):
                setattr(f, k, kwds[k])
        return f
    return decorator


@autograph(author='qiuchen', date='2021-01-28')
def func(a, c):
    print(a+c)


from dataclasses import dataclass


@dataclass
class Point(object):
    x: str
    y: str


if __name__ == '__main__':
    func(3, 6)
    print(func.author)
    print(func.date)
    print(func.__name__)

    p1 = Point(2, 4)
    p2 = Point(2, 4)
    print(p1 == p2)
