#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
__title__ = ''
__author__ = 'JWH5566'
__mtime__ = '2016/3/24'

# >>> from operator import itemgetter
# >>> a = [(5, 3), (1, 3), (1, 2), (2, -1), (4, 9)]
# >>> sorted(a)  # 默认按照元祖的元素依次排序
# [(1, 2), (1, 3), (2, -1), (4, 9), (5, 3)]
# >>> sorted(a, key=itemgetter(0))  #  按照元祖的第一个元素排序 其他按照原来元祖的顺序
# [(1, 3), (1, 2), (2, -1), (4, 9), (5, 3)]
# >>> sorted(a, key=itemgetter(0, 1))  #  类似默认
# [(1, 2), (1, 3), (2, -1), (4, 9), (5, 3)]
# >>> sorted(a, key=itemgetter(1))
# [(2, -1), (1, 2), (5, 3), (1, 3), (4, 9)]
# >>> sorted(a, key=itemgetter(1), reverse=True)
# [(4, 9), (5, 3), (1, 3), (1, 2), (2, -1)]
