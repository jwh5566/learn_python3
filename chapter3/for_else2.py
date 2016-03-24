#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
__title__ = ''
__author__ = 'JWH5566'
__mtime__ = '2016/3/24'


class DriverException(Exception):
    pass


people = [('蒋文华', 16), ('蒋梦丽', 17), ('蒋玉华', 16)]
for person, age in people:
    if age >= 18:
        driver = (person, age)
        break
else:
    raise DriverException('没有发现司机')
