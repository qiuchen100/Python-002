import multiprocessing
from os import getppid
import time
from multiprocessing import Process
import os


class NewProcess(Process):
    def __init__(self, num):
        self.num = num
        super().__init__()

    def run(self):
        while True:
            print(f'我是进程{self.num}，我的pid是：{os.getpid()}\n')
            time.sleep(1)


if __name__ == "__main__":
    for i in range(2):
        p = NewProcess(i)
        p.start()
