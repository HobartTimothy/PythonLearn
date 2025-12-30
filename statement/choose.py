"""
Description: Python 分支结构学习包

Author: Robert.HU

Version: 1.0
"""


def check_even_odd(number):
    """
    使用三元运算符判断奇偶数
    :param number: 数字
    :return: 奇偶性
    """
    print("                     === 奇偶判断 ===                     ")

    result = "偶数" if number % 2 == 0 else "奇数"
    print(f'{number} 是 {result}')
    print("")
    return result


def max_value(a, b):
    """
    :param a: 数字
    :param b: 数字
    :return: 最大值
    """

    print("                     === 最大值计算 ===                     ")

    result = a if a >=b else b
    print(f'{a} 和 {b} 的最大值是: {result}')
    print("")
    return result


def bmi_calculator(height, weight):
    """
    :param height: 身高
    :param weight: 体重
    :return: BMI指数
    """

    print("                     === BMI 计算器 ===                     ")
    bmi = weight / (height / 100) ** 2
    print(f'当前输入身高:{height = :.1f}, 当前输入体重:{weight = :.1f}, BMI指数: {bmi = :.1f}')

    if bmi < 18.5:
        print('过轻')
    elif bmi < 24:
        print('正常')
    elif bmi < 27:
        print('过重')
    elif bmi < 35:
        print('肥胖')
    else:
        print(' 过度肥胖 ')

    print("")


def list_match(args):
    """
    :param args: 输入参数
    :return: 输出参数
    """
    print("                     === 列表匹配 ===                     ")
    match args:
        case ['gcc']:
            print('gcc: missing source file(s).')
        case ['gcc', file1, *files]:
            print('gcc compile: ' + file1 + ', ' + ', '.join(files))
        case ['clean']:
            print('clean')
        case _:
            print('invalid command.')
    print("")



def login_check(username, password, is_admin=False):
    """
    用户登录验证
    :param username: 用户名
    :param password: 密码
    :param is_admin: 是否为管理员
    :return: 登录结果
    """
    print("                     === 登录验证 ===                     ")

    if username and password:
        if username == "admin" and password == "123456":
            if is_admin:
                print("管理员登录成功")
            else:
                print("普通用户登录成功")
        elif username == "guest" and password == "guest":
            print("访客登录成功")
        else:
            print("用户名或密码错误")
    else:
        print("请输入用户名和密码")

    print("")



def http_status_code(code):
    """
    :param code: HTTP状态码
    :return: HTTP状态码对应的信息
    """

    print("                     === HTTPCODE ===                     ")

    match code:
        case 400:
            description = 'Bad Request'
        case 401:
            description = 'Unauthorized'
        case 403:
            description = 'Forbidden'
        case 404:
            description = 'Not Found'
        case 405:
            description = 'Method Not Allowed'
        case 418:
            description = 'I am a teapot'
        case 429:
            description = 'Too many requests'
        case _:
            description = 'Unknown Status Code'

    print(f'输入的HTTP状态码: {code}. 状态码描述: {description}')
    print("")