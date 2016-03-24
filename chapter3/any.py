#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
__title__ = ''
__author__ = 'JWH5566'
__mtime__ = '2016/3/24'

items = [0, None, 0.0, False, 0, 7]
found = False
for item in items:
    print('扫描列表项')
    if item:
        found = True
        break
if found:
    print('列表中至少有一项为True')
else:
    print('列表中所有项都为False')
