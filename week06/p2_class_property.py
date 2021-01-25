class Human(object):
    live = True

    def __init__(self, name):
        self.name = name


man = Human('Adam')
woman = Human('Eve')

print(Human.__dict__)
print(man.__dict__)
