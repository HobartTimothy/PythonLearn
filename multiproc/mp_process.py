import os
import os, time, random

def run_proc(name):
    """
    :description 简单子进程
    :param name:
    :return:
    """
    print('子进程 %s (%s)' % (name, os.getpid()))

def long_time_proc(name):
    """
    :description 耗时进程
    :param name:
    :return:
    """

    print('子进程 %s (%s) 开始执行' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('子进程 %s .执行时间: %0.2f (秒).' % (name, (end - start)))
