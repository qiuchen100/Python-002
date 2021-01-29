# -*- coding: utf-8 -*-


def hi(self):
    print('Hi metaclass')


# type的三个参数：类名、父类的元组、类的成员
Foo = type('Foo', (), {'say_hi':hi})
foo = Foo()
foo.say_hi()


def pop_value(self, dict_value):
    for key in self.keys():
        if self.__getitem__(key) == dict_value:
            self.pop(key)
            break


# 元类要求：必须继承自type
class DelValue(type):
    def __new__(cls, name, bases, attrs):
        attrs['pop_value'] = pop_value
        return type.__new__(cls, name, bases, attrs)


class DelDictValue(dict, metaclass=DelValue):
    pass

d = DelDictValue()
d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d.pop_value('C')
print(d)

