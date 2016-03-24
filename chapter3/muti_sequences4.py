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
for data in zip(people, ages, cities):
    person, age, city = data
    print(person, age, city)
