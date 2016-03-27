#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
__title__ = ''
__author__ = 'JWH5566'
__mtime__ = '2016/3/27'

items = 'ABCDE'
pairs = [(items[a], items[b])
         for a in range(len(items)) for b in range(a, len(items))]
print(pairs)
