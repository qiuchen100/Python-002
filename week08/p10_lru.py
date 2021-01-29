# -*- coding: utf-8 -*-

from functools import lru_cache


@lru_cache()
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    import timeit
    print(timeit.timeit("fibonacci(6)", setup='from __main__ import fibonacci'))

