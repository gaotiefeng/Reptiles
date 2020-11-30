import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
# encoding: utf-8

# 多进程不共享全局变量
import multiprocessing
import time
import os

def write(q):
        print("write启动(%s)，父进程为(%s)" % (os.getpid(), os.getppid()))
        for i in "pythontest":
                q.put(i)


def read(q):
        print("read启动(%s)，父进程为(%s)" % (os.getpid(), os.getppid()))
        for i in range(q.qsize()):
                print("read从Queue获取到消息：%s" % q.get(True))


def main():
    print("(%s) start" % os.getpid())
    q = multiprocessing.Manager().Queue()
    po = multiprocessing.Pool()
    po.apply_async(write, args=(q,))

    time.sleep(2)

    po.apply_async(read, args=(q,))
    po.close()
    po.join()

    print("(%s) end" % os.getpid())
