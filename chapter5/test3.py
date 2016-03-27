#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
__title__ = ''
__author__ = 'JWH5566'
__mtime__ = '2016/3/27'


def counter(start=0):
    n = start
    while True:
        result = yield n  # A
        print(type(result), result)  # B
        if result == 'Q':
            break
        n += 1


c = counter()
print(next(c))  # C
print(c.send('Wow!'))  # D
print(next(c))  # E
print(c.send('Q'))  # F
