#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
__title__ = ''
__author__ = 'JWH5566'
__mtime__ = '2016/3/27'


class Fun:
    def __init__(self, s):
        self._s = s

    def __len__(self):
        return len(self._s)

    def __bool__(self):
        return '42' in self._s


fun = Fun('Hello! I am 9 years old!')
print(len(fun))
print(bool(fun))

fun2 = Fun('Hello! I am 42 years old!')
print(len(fun2))
print(bool(fun2))
