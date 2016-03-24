#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
__title__ = ''
__author__ = 'JWH5566'
__mtime__ = '2016/3/24'

from itertools import count

for n in count(5, 3):  # count 执行加法，返回迭代器
    if n > 20:
        break
    print(n, end=',')
