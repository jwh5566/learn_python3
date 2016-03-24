#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
__title__ = ''
__author__ = 'JWH5566'
__mtime__ = '2016/3/24'


class Person:
    def __init__(self, age):
        self.age = age


fab = Person(age=39)
print(fab.age, id(fab))
fab.age = 29
print(fab.age, id(fab))
