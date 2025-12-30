"""
Description: Python 循环结构学习包

Author: Robert.HU

Version: 1.0
"""
import time


def countdown(n):
    """
    :param n: 数字
    :return:
    """

    print(f"输入数字: {n}")
    for i in range(n):
        print(i)


def countdown2(n):
    """
    :param n: 数字
    :return:
    """

    print(f"输入数字: {n}")
    for i in range(1, n, 2):
        print(i)


def count_num(n):

    total = 0

    for i in range (1, n):
        total += i

    print(f"输入数字: {n}, 总和: {total}")
    return total


def count_num2(n):
    total = 0
    for i in range (1, n, 3):
        if i % 2 == 0:
            total += i

    print(f"输入数字: {n}, 总和: {total}")


def multi_table():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print(f'{i}×{j}={i * j}', end='\t')
        print()