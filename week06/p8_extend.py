# -*- coding: utf-8 -*-
class Person(object):
    def walk(self):
        print('Person walk')


class Man(Person):
    def walk(self):
        print('Man walk')


class Women(object):
    def walk(self):
        print('Women walk')


class Son(Man, Women):
    pass


son = Son()
son.walk()
print(Son.mro())


class PoliceMan(Man):
    pass


class PoliceWomen(Women):
    def walk(self):
        print('PoliceWomen walk')

class LitlePolice(PoliceMan, PoliceWomen):
    pass

litlePolice = LitlePolice()
litlePolice.walk()
print(LitlePolice.mro())