# Author: by tunan
# Date: 2022/7/10 14:57
# Function:

# 线程池：一次性开辟一些线城。我们用户直接给线程池子提交任务。 线程任务的调度交给下线程池来完成

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from multiprocessing import Process, Pool


def fn(name):
    for i in range(1000):
        print(name, i)


if __name__ == '__main__':

    # # 创建线程池
    # with ThreadPoolExecutor(50) as t:
    #     for i in range(100):
    #         t.submit(fn, name=f'线程{i}')
    # # 等待线程池中的任务全部执行完毕，才能继续执行下面的语句（守护）
    # print('end')

    # 创建进程池
    pool = Pool(processes=50)
    for i in range(100):
        pool.apply_async(func=fn, args=('进程%d'%i,))
    pool.close()
    pool.join()







