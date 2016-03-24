#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
__title__ = ''
__author__ = 'JWH5566'
__mtime__ = '2016/3/24'

n = 39
remainders = []
while n > 0:
    n, remainder = divmod(n, 2)
    remainders.append(str(remainder))
remainders = remainders[::-1]
str = ''.join(remainders)
print(str)
