#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    自定义迭代器
"""
__title__ = ''
__author__ = 'JWH5566'
__mtime__ = '2016/3/27'


class OddEven:
    def __init__(self, data):
        self._data = data
        self.indexes = (list(range(0, len(data), 2)) +
                        list(range(1, len(data), 2)))

    def __iter__(self):
        return self

    def __next__(self):
        if self.indexes:
            return self._data[self.indexes.pop(0)]
        raise StopIteration


oddeven = OddEven('ThIsIsCoOl!')
print(''.join(c for c in oddeven))
