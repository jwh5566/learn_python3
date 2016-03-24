#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
__title__ = ''
__author__ = 'JWH5566'
__mtime__ = '2016/3/24'

alert_system = 'console'
error_severity = 'critical'
error_message = 'OMG!一些严重的事情发生了!'

if alert_system == 'console':
    print(error_message)
elif alert_system == 'email':
    if error_severity == 'critical':
        pass
        # send_email('admin@example.com', error_message)
    elif error_severity == 'medium':
        pass
        # send_mail('support1@example.com', error_message)
    else:
        pass
        # send_mail('support2@example.com', error_message)
