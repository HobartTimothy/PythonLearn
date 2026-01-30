import os
from multiprocessing import Process
from multiprocessing import Pool

from statement import choose
from statement import choose_use
from statement import loop
from multiproc import mp_process

# 循环
"""
if __name__ == '__main__':
    choose.http_status_code(5000)

    choose.max_value(11, 60)

    choose.bmi_calculator(170, 70)

    choose.list_match(['gcc', 'a.c', 'b.c', 'c.c', 'e.c', 'f.c'])

    choose.login_check('admin', '123456', True)


    choose_use.segment_function(0.5)
    choose_use.score_function(10090)

    test_list = [10, 11, 15, 20, 22, 33, 47, 55, 50, 61, 71, 76, 73, 81, 90, 91, 100, 101]
    even_odd_list = map(choose.check_even_odd, test_list)
    print(list(even_odd_list))

    # loop.countdown(3600)
    # loop.countdown2(3600)
    # loop.count_num(3600)
    # loop.count_num2(3600)
    # loop.multi_table()
"""

if __name__ == '__main__':
    # print('父进程 %s.' % os.getpid())
    # p = Process(target=mp_process.run_proc, args=('test',))
    # print('子进程开始.')
    # p.start()
    # p.join()
    # print('子进程结束.')

    p = Pool(4)

    print('父进程 %s.' % os.getpid())
    for i in range(5):
        p.apply_async(mp_process.long_time_proc, args=(i,))
    print('等待所有子进程执行结束')
    # 对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。
    p.close()
    p.join()
    print('所有子进程执行完成')