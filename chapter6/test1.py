#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
__title__ = ''
__author__ = 'JWH5566'
__mtime__ = '2016/3/27'

from time import sleep, time


def f():
    sleep(0.3)


def g():
    sleep(0.5)


def measure(func):
    t = time()
    func()
    print(func.__name__, 'took:', time() - t)


measure(f)
measure(g)
