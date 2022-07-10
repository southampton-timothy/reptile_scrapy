# Author: by tunan
# Date: 2022/7/10 11:13
# Function:

# 多线程
from threading import Thread

# 方法一：
# def func():
#     for i in range(1000):
#         print('func', i)
#
#
# if __name__ == '__main__':
#     t = Thread(target=func)  # 创建线程并给线程安排任务
#     t.start()  # 多线程状态为可以开始工作状态，具体的执行时间由cpu决定
#
#     # t2 = Thread()  创建第二个线程
#     # t2.start()
#     for i in range(1000):
#         print('main', i)


# 方法二：创建一个类
class MyThread(Thread):

    def _init_(self, name):
        self.name = name

    def run(self):  # 固定的 ——> 当线程被执行的时候，被执行的就是run()
        for i in range(1000):
            print(self.name, i)


if __name__ == '__main__':
    t = MyThread(name='周杰伦')
    t.start()  # 开启线程

    t2 = MyThread(name='林俊杰')
    t2.start()
    # for i in range(1000):
    #     print("主进程", i)

# def func(name):
#     for i in range(1000):
#         print(name, i)
#
#
# if __name__ == '__main__':
#     t1 = Thread(target=func, args=('周杰伦',))  # 传递参数必须是元组
#     t1.start()
#     t2 = Thread(target=func, args=('林俊杰',))
#     t2.start()