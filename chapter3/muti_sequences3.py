#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
__title__ = ''
__author__ = 'JWH5566'
__mtime__ = '2016/3/24'

people = ['蒋文华', '蒋梦丽', '蒋玉华']
ages = [25, 26, 27]
cities = ['南京', '镇江', '常州']
for person, age, city in zip(people, ages, cities):  # zip 函数返回一个元祖对象
    print(person, age, city)
