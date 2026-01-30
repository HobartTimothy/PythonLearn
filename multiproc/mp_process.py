import os

def run_proc(name):
    print('子进程 %s (%s)' % (name, os.getpid()))
