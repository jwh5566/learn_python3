#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
__title__ = ''
__author__ = 'JWH5566'
__mtime__ = '2016/3/29'

import base64

import requests

img_data = requests.get('http://127.0.0.1:8000').content
b64_img_data = base64.b64encode(img_data)
print(b64_img_data)
print('*' * 40)
str_img_data = b64_img_data.decode('utf-8')
print(str_img_data)
