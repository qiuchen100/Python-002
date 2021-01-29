# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class Base(metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        pass

    @abstractmethod
    def bar(self):
        pass


class Concrete(Base):
    def foo(self):
        print('foo')

    def bar(self):
        print('bar')


c = Concrete()
