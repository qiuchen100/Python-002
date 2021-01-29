# -*- coding: utf-8 -*-


class Human(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def getName(self):
        return self.name

    def getGender(self):
        return self.gender


class Man(Human):
    def __init__(self, name):
        print(f'Hi, man {name}')


class Women(Human):
    def __init__(self, name):
        print(f'Hi, women {name}')


class Factory:
    def getPerson(self, name, gender):
        if gender == 'M':
            return Man(name)
        elif gender == 'F':
            return Women(name)
        else:
            return


def factory2(func):
    class klass: pass
    setattr(klass, func.__name__, func)
    return klass


def say_foo(self):
    print('bar')


if __name__ == '__main__':
    factory = Factory()
    person = factory.getPerson("Adam", "M")

    Foo = factory2(say_foo)
    foo = Foo()
    foo.say_foo()
    