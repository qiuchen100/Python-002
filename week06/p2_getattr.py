class Human2(object):
    """
    属性不在实例中时,__getattr__会被调用
    """
    pass

    def __init__(self):
        """
        docstring
        """
        self.age = 18

    def __getattr__(self, item):
        """
        docstring
        """
        print(f'__getattr__ called item: {item}')
        return "ok"


h1 = Human2()
print(h1.age)
print(h1.noattr)
