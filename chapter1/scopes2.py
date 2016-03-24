#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
__title__ = ''
__author__ = 'JWH5566'
__mtime__ = '2016/3/24'


# 本地变量和全局变量
def local():
    # 本地范围没有找到根据LEGB原则寻找
    print(m, '这里是本地变量的M')


m = 5
print(m, '这里是全局变量的M')
local()
