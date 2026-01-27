
# 分段函数
def segment_function(x):
    """
    :param x: 输入参数
    :return: 输出参数
    """

    print("                     分段函数计算                     ")

    if x > 1:
        y = 3 * x - 5
    elif x >= -1:
        y = 2 ** x + 1
    else:
        y = 0

    print(f'输入的参数: {x = :.2f}, 输出的参数: {y = :.2f}')
    print("")

    return y


def score_function(score):
    """
    :param score: 输入参数
    :return: 输出参数
    """

    print("                     分数函数计算                     ")
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'

    print(f'输入的参数: {score = :.2f}, 输出的参数: {grade}')