
class Human(object):
    """
    docstring
    """

    def __init__(self):
        """
        docstring
        """
        self.age = 18

    def __getattribute__(self, item):
        """
        截获用户获取实例属性的行为
        """
        # print(f'__getattribute__ called item: {item}')
        # return super().__getattribute__(item)
        try:
            return super().__getattribute__(item)
        except Exception as e:
            self.__dict__[item] = 100
            return self.item


h1 = Human()
print(h1.age)
print(h1.name)
