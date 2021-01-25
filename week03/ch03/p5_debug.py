import sys
import multiprocessing
from os import getppid
import time
from multiprocessing import Process
import os


def debug_info(title):
    print('-' * 20)
    print(title)
    print('模块名称：', __name__)
    print('父进程：', os.getppid())
    print('当前进程：', os.getpid())
    print('-' * 20)


def f(name):
    debug_info('function f')
    print('hello, ', name)


# def run():
#     print("子进程开启")
#     time.sleep(2)
#     print("子进程结束")


if __name__ == "__main__":
    debug_info('function main')
    p = Process(target=f, args=('Bob', ))
    p.start()

    for p in multiprocessing.active_children():
        print(f'子进程名称: {p.name}  id: {str(p.pid)}')
    print('进程结束')
    print(f'CPU核心数量：{str(multiprocessing.cpu_count())}')
    p.join()
