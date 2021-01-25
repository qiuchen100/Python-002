def f1():
    1/0


def f2():
    list1 = []
    list1[1]
    f1()


def f3():
    f2()


f3()
# try:

# except (ZeroDivisionError, Exception) as e:
#     print(e)
