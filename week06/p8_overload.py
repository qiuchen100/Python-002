# -*- coding: utf-8 -*-
class Kclass(object):
    def A(self):
        pass

    def A(self, a, b):
        print(f'{a} - {b}')

# Python没有实现重载功能
k = Kclass()
k.A()