# -*- coding: utf-8 -*-


class Displayer(object):
    def display(self, message):
        print(message)


class LoggerMixin():
    def log(self, message, filename='logfile.txt'):
        with open(filename, 'a+') as fh:
            fh.write(message)

    def display(self, message):
        super(LoggerMixin, self).display(message)
        self.log(message)


class MySubClass(LoggerMixin, Displayer):
    def log(self, message):
        super().log(message, filename='subclasslog.txt')


subClass = MySubClass()
subClass.display("This string will be shown and logged in subclasslog.txt")
print(MySubClass.mro())

