#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
__title__ = ''
__author__ = 'JWH5566'
__mtime__ = '2016/3/27'

students = [
    dict(id=0, credits=dict(math=9, physics=6, history=7)),
    dict(id=1, credits=dict(math=6, physics=7, latin=10)),
    dict(id=2, credits=dict(history=8, physics=9, chemistry=10)),
    dict(id=3, credits=dict(math=5, physics=5, geography=7)),
]


# 装饰学生对象
def decorate(student):
    return (sum(student['credits'].values()), student)


# 解装饰
def undecorate(decorate_student):
    return decorate_student[1]


students = sorted(map(decorate, students), reverse=True)
print(students)
print('*' * 20)
#  排序之后 解装饰
students = list(map(undecorate, students))
print(students)
