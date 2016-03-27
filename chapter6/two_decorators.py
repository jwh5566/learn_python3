#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
__title__ = ''
__author__ = 'JWH5566'
__mtime__ = '2016/3/27'

from time import time
from functools import wraps


def measure(func):
    @wraps(func)  # 保持原函数的属性 而不是wrapper的
    def wrapper(*args, **kwargs):
        t = time()
        result = func(*args, **kwargs)
        print(func.__name__, 'took:', time() - t)
        return result

    return wrapper


def max_result(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result > 100:
            print('Result is too big ({0}). Max allowed is 100.'.format(result))
        return result

    return wrapper


@max_result
@measure  # 装饰点
def cube(n):
    return n ** 3


print(cube(3))
print(cube(5))
