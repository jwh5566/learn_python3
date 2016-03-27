#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
__title__ = ''
__author__ = 'JWH5566'
__mtime__ = '2016/3/27'


def fibonacci(N):
    yield 0
    if N == 0:
        return
    a = 0
    b = 1
    while b < N:
        yield b
        a, b = b, a + b


print(list(fibonacci(0)))
print(list(fibonacci(50)))
