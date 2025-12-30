import logging


__name__ = "Python函数学习教程包"

__all_list__ = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 设置包级别的日志记录器
logging.getLogger(__name__).addHandler(logging.NullHandler())