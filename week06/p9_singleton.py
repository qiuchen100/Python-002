# -*- coding: utf-8 -*-

def singleton(cls):
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance


@singleton
class MyClass:
    pass


m1 = MyClass()
m2 = MyClass()
print(id(m1))
print(id(m2))


class MyClass2(object):
    __singleton_class = None

    def __new__(cls, *args, **kwargs):
        if cls.__singleton_class is None:
            cls.__singleton_class = super(MyClass2, cls).__new__(
                cls)
        return cls.__singleton_class

    def __init__(self, name):
        self.name = name


m11 = MyClass2('tt')
m22 = MyClass2('xx')
print(id(m11))
print(id(m22))


# 加锁版
import threading
class MyClass3(object):
    __singleton_class = None
    locker = threading.Lock()
    def __new__(cls, *args, **kwargs):
        cls.locker.acquire()
        try:
            if cls.__singleton_class is None:
                cls.__singleton_class = super(MyClass3, cls).__new__(
                    cls)
            return cls.__singleton_class
        finally:
            cls.locker.release()

    def __init__(self, name):
        self.name = name

m111 = MyClass3('tt')
m222 = MyClass3('xx')
print(id(m111))
print(id(m222))