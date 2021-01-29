# -*- coding: utf-8 -*-
# __getattribute__的底层原理是描述器
class Desc(object):
    """
    通过打印来展示描述器的访问流程
    """

    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        print(f'__get__ {instance} {owner}')
        return self.name

    def __set__(self, instance, value):
        print(f'__set__ {instance} {value}')
        self.name = value

    def __delete__(self, instance):
        print(f'__delete__ {instance}')
        del self.name


class MyObj(object):
    a = Desc('aaa')
    b = Desc('bbb')


my_obj = MyObj()
print(my_obj.a)


my_obj.a = 456
print(my_obj.a)
