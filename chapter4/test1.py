#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
__title__ = ''
__author__ = 'JWH5566'
__mtime__ = '2016/3/25'
x = [1, 2, 3]


def func(x):
    x[1] = 42
    x = 'aaaaaaa'
    print(id(x))


print(id(x))
func(x)

print(id(x))
