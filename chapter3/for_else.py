#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
__title__ = ''
__author__ = 'JWH5566'
__mtime__ = '2016/3/24'


class DriverException(Exception):
    pass


people = [('蒋文华', 26), ('蒋梦丽', 17), ('蒋玉华', 26)]
driver = None
for person, age in people:
    if age >= 18:
        driver = (person, age)
        break
if driver is None:
    raise DriverException('没有发现司机')
else:
    print('司机是', driver[0])
