import datetime


class Kls1(object):
    bar = 1

    def foo(self):
        print('in foo')

    @classmethod
    def class_foo(cls):
        print(cls.bar)
        print(cls.__name__)
        cls().foo()


Kls1.class_foo()
print(__name__)


class Story(object):

    snake = 'Python'

    def __init__(self, name):
        self.name = name

    @classmethod
    def get_apple_to_eve(cls):
        return cls.snake

    @staticmethod
    def god_come_go():
        if datetime.datetime.now().month % 2:
            print('god is coming')


s = Story('anyone')
print(s.get_apple_to_eve())
print(Story.get_apple_to_eve())
