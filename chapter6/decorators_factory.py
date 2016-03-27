#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
__title__ = ''
__author__ = 'JWH5566'
__mtime__ = '2016/3/27'

from functools import wraps


def max_result(threshold):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result > threshold:
                print('Result is too big ({0}). Max allowed is {1}.'
                      .format(result, threshold))
            return result

        return wrapper

    return decorator


@max_result(75)
def cube(n):
    return n ** 3


print(cube(5))
