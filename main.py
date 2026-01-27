from statement import choose
from statement import choose_use
from statement import loop


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
"""

if __name__ == '__main__':
    # loop.countdown(3600)
    # loop.countdown2(3600)
    # loop.count_num(3600)
    # loop.count_num2(3600)
    loop.multi_table()
