# 参数
# - group 分组 很少用
# - target 调用对象
# - name 别名
# - args 被调用对象的位置参数元组
# - kwargs 表示调用对象的字典

from multiprocessing import Process


def my_fun(name):
    print(f'hello {name}')


if __name__ == "__main__":
    p = Process(target=my_fun, args=('john',))
    p.start()
    p.join()
