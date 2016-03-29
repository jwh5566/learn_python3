#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
__title__ = ''
__author__ = 'JWH5566'
__mtime__ = '2016/3/29'

import requests

page = requests.get('http://127.0.0.1:8000/img/owl-alcohol.png')
print(page.content)


# img/owl-alcohol.png
