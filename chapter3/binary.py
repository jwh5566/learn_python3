#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
__title__ = ''
__author__ = 'JWH5566'
__mtime__ = '2016/3/24'
# 打印整数的二进制形式
n = 39
remainders = []
while n > 0:
    remainder = n % 2
    remainders.append(str(remainder))
    n //= 2
# 反向打印列表序列
remainders = remainders[::-1]
str = ''.join(remainders)  # join方法需要序列值是字符串类型
print(str)
