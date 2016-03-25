#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
__title__ = ''
__author__ = 'JWH5566'
__mtime__ = '2016/3/25'


def outer():
    test = 1

    def inner():
        nonlocal test
        test = 2
        print('inner:', test)

    inner()
    print('outer: ', test)


test = 0
outer()
print('globle: ', test)
