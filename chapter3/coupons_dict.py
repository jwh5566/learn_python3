#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   使用dict来保存和使用customers信息
"""
__title__ = ''
__author__ = 'JWH5566'
__mtime__ = '2016/3/24'

customers = [
    dict(id=1, total=200, coupon_code='F20'),
    dict(id=2, total=150, coupon_code='P30'),
    dict(id=3, total=100, coupon_code='P50'),
    dict(id=4, total=110, coupon_code='F15'),
]
discounts = {
    'F20': (0.0, 20.0),
    'P30': (0.3, 0.0),
    'P50': (0.5, 0.0),
    'F15': (0.0, 15.0),
}

for customer in customers:
    code = customer['coupon_code']
    percent, fixed = discounts.get(code, (0.0, 0.0))  # 如果code不在 discounts 那么返回（0.0， 0.0）表示不打折，没有优惠
    customer['discount'] = percent * customer['total'] + fixed

for customer in customers:
    print(customer['id'], customer['total'], customer['discount'])
