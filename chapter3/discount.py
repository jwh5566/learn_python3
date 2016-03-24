#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    今天过期的商品打折20%
"""
__title__ = ''
__author__ = 'JWH5566'
__mtime__ = '2016/3/24'

from datetime import date, timedelta

today = date.today()
tomorrow = today + timedelta(days=1)
products = [
    {'sku': '1', 'expiration_date': today, 'price': 100.0},
    {'sku': '2', 'expiration_date': tomorrow, 'price': 50},
    {'sku': '3', 'expiration_date': today, 'price': 20},
]
print('今天过期的商品打折20%')
for product in products:
    if product['expiration_date'] != today:
        continue
    product['price'] *= 0.8
    print(
        'sku的价格', product['sku'], '现在是', product['price']
    )
