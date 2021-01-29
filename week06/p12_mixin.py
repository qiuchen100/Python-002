# -*- coding: utf-8 -*-


def mixin(Klass, MixinKlass):
    Klass.__bases__ = (MixinKlass,) + Klass.__bases__


class Fclass(object):
    def test(self):
        print('in FatherClass')


class S1class(Fclass):
    pass


class Mixinclass(object):
    def test(self):
        print('in Mixinclass')


class S2class(S1class, Mixinclass):
    pass


print(f' test1 : S1class MRO : {S1class.mro()}')
s1 = S1class()
s1.test()

print('-' * 100)

mixin(S1class, Mixinclass)
print(f' test2 : S1class mixin MRO : {S1class.mro()}')
s1 = S1class()
s1.test()

print('-' * 100)

print(f' test3 : S2class MRO : {S2class.mro()}')
s2 = S2class()
s2.test()