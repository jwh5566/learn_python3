#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
__title__ = ''
__author__ = 'JWH5566'
__mtime__ = '2016/3/27'
from time import sleep, time


def f(sleep_time=0.1):
    sleep(sleep_time)


def measure(func, *args, **kwargs):
    t = time()
    func(*args, **kwargs)
    print(func.__name__, 'took:', time() - t)


measure(f, 0.2)
measure(f, sleep_time=0.3)
