#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
__title__ = ''
__author__ = 'JWH5566'
__mtime__ = '2016/3/24'
s = 'my name is 蒋文华'
print(type(s))
encoded_s = s.encode('utf-8')  # 编码
print(encoded_s)
print(type(encoded_s))  # 编码之后是字节类型
orgin_s = encoded_s.decode('utf-8')  # 解码
print(orgin_s)
print(type(orgin_s))
