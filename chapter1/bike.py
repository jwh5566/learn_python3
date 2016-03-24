#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    理解类 和 对象
"""
__title__ = ''
__author__ = 'JWH5566'
__mtime__ = '2016/3/24'


class Bike():
    def __init__(self, colour, frame_materil):
        self.colour = colour
        self.frame_material = frame_materil

    def brake(self):
        print('骑车咯！')


# 创建2个实例
red_bike = Bike('Red', 'Carbon fiber')
blue_bike = Bike('Blue', 'Steel')

print(red_bike.colour)
print(red_bike.frame_material)
print(blue_bike.colour)
print(blue_bike.frame_material)
red_bike.brake()
