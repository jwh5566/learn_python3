#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
__title__ = ''
__author__ = 'JWH5566'
__mtime__ = '2016/3/24'


# 本地，封闭， 全局的变量
def enclosing_fun():
    m = 13

    def local():
        print(m, '这里是本地范围的M')  # 本地没有找到相上寻找，在封闭的函数 找到

    local()


m = 5
print(m, '这里是全局范围的M')
enclosing_fun()
