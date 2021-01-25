# 区分父子进程
import os
import time

res = os.fork()
print(f'res == {res}')

if res == 0:
    print(f'我是子进程，我的PID是：{os.getpid()}，我的父进程的PID是：{os.getppid()}')
else:
    print(f'我是父进程，我的PID是：{os.getpid()}')
