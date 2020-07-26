#!/usr/bin/env python
# -*- coding: utf-8 -*-


def chain(num):
    for i in range(num):
        yield i


num = 5
y = chain(num)
print(next(y))
print(next(y))
print(list(y))


mylist = []
for i in range(1, 11):
    if i > 5:
        mylist.append(i**2)
print(mylist)

# 这种推导式的方式和上面那种等价
mylist2 = [i**2 for i in range(1, 11) if i > 5]
print(mylist2)

# 生成字典
mydict = {i: i * i for i in range(5)}
print(mydict)

# 生成集合
myset = {i**2 for i in range(1, 11) if i > 5}
print(myset)

# 生成生成器
mygen = (i**2 for i in range(1, 11) if i > 5)
print(mygen)
print(list(mygen))

# 生成元组
mytuple = tuple(i**2 for i in range(1, 11) if i > 5)
print(mytuple)


# 循环嵌套
mylist = [str(i) + j for i in range(5) for j in 'ABCDEF']
print(mylist)
